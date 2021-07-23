# pylint: disable = no-self-use, protected-access

"""User API

    This API namespace defines CRUD operations for users.

    Endpoints
    ----------
    /api/profile/user : GET
        Get user by ID.
    /api/profile/user : PUT
        Create user with JSON object.
    /api/profile/user : PATCH
        Update user by ID with JSON-encoded key-value pairs.
    /api/profile/user : DELETE
        Delete user by ID.
    /api/profile/user/all : GET
        Get all users.

"""

from http import HTTPStatus
from bson import ObjectId

from bson.errors import InvalidId
from umongo import ValidationError

from flask import request
from flask_restx import Namespace, Resource
from utils.flask_accepts import accepts, responds

# from app.http.api.utils.security import csrf_protection

from app.db.profile.user.manager import UserManager
from app.db.profile.user import User, UserSchema

api = Namespace("user", description="User related operations.")


@api.route("/")
class UserResource(Resource):
    """
    Resource for handling single-user operations.
    """

    @api.doc(description="Get user by ID.")
    @accepts(dict(name="_id", type=str), api=api)
    @responds(schema=UserSchema, api=api)
    @api.doc(
        responses={
            HTTPStatus.FOUND: "Successfully retrieved user.",
            HTTPStatus.BAD_REQUEST: "Unspecified ID / specified ID is invalid.",
            HTTPStatus.NOT_FOUND: "User with specified ID doesn't exist.",
        }
    )
    def get(self):
        """
        Get user by ID.
        """
        if not request.parsed_args["_id"]:
            api.abort(
                HTTPStatus.BAD_REQUEST, message="Cannot get user by unspecified ID."
            )
        try:
            _id = ObjectId(request.parsed_args["_id"])
            user = UserManager.get(_id)
        except (ValidationError, InvalidId) as error:
            api.abort(HTTPStatus.BAD_REQUEST, message=error.args[0])
        if not user:
            api.abort(
                HTTPStatus.NOT_FOUND,
                message="User with specified ID: {} doesn't exist".format(_id),
            )
        return user

    # @csrf_protection
    @api.doc(description="Create user with JSON object.")
    @accepts(schema=UserSchema, partial=User.REQUIRED_ON_CREATE, api=api)
    @responds(schema=UserSchema, api=api)
    @api.doc(
        responses={
            HTTPStatus.FOUND: "Successfully created user.",
            HTTPStatus.BAD_REQUEST: "Invalid user JSON object specified.",
        }
    )
    def put(self):
        """
        Create user with JSON object.
        """
        try:
            user = UserManager.create(User(**request.parsed_obj))
        except ValidationError as error:
            api.abort(HTTPStatus.BAD_REQUEST, message=error.args[0])
        return user

    # @csrf_protection
    @api.doc(description="Update user by ID with JSON-encoded key-value pairs.")
    @accepts(
        dict(name="_id", type=str),
        schema=UserSchema,
        partial=True,
        api=api,
    )
    @responds(schema=UserSchema, api=api)
    @api.doc(
        responses={
            HTTPStatus.FOUND: "Successfully updated user.",
            HTTPStatus.BAD_REQUEST: "Invalid user fields specified in updates.",
        }
    )
    def patch(self):
        """
        Update user by ID with JSON-encoded key-value pairs.
        """
        if not request.parsed_args["_id"]:
            api.abort(
                HTTPStatus.BAD_REQUEST, message="Cannot update user by unspecified ID."
            )
        try:
            _id = ObjectId(request.parsed_args["_id"])
            user = UserManager.get(_id)
        except (ValidationError, InvalidId) as error:
            api.abort(HTTPStatus.BAD_REQUEST, message=error.args[0])
        if not user:
            api.abort(
                HTTPStatus.NOT_FOUND,
                message="User with specified ID: {} doesn't exist".format(_id),
            )
        try:
            user = UserManager.update(_id, request.parsed_obj)
        except ValidationError as error:
            api.abort(HTTPStatus.BAD_REQUEST, message=error.args[0])
        return user

    @api.doc(description="Delete user by ID.")
    @accepts(dict(name="_id", type=str), api=api)
    @responds(schema=UserSchema, api=api)
    @api.doc(
        responses={
            HTTPStatus.FOUND: "Successfully deleted user.",
            HTTPStatus.BAD_REQUEST: "Unspecified ID / specified ID is invalid.",
            HTTPStatus.NOT_FOUND: "User with specified ID doesn't exist.",
        }
    )
    def delete(self):
        """
        Delete user by ID.
        """
        if not request.parsed_args["_id"]:
            api.abort(
                HTTPStatus.BAD_REQUEST, message="Cannot delete user by unspecified ID."
            )
        try:
            _id = ObjectId(request.parsed_args["_id"])
            user = UserManager.get(_id)
        except (ValidationError, InvalidId) as error:
            api.abort(HTTPStatus.BAD_REQUEST, message=error.args[0])
        if not user:
            api.abort(
                HTTPStatus.NOT_FOUND,
                message="User with specified ID: {} doesn't exist".format(_id),
            )
        try:
            user = UserManager.delete(_id)

        except ValidationError as error:
            api.abort(HTTPStatus.BAD_REQUEST, message=error.args[0])
        return user


@api.route("/all")
class UsersResource(Resource):
    """
    Resource for handling multi-user operations.
    """

    @api.doc(description="Get all users.")
    @accepts(api=api)
    @responds(schema=UserSchema(many=True), api=api)
    @api.doc(
        responses={
            HTTPStatus.FOUND: "Successfully retrieved all users.",
            HTTPStatus.NOT_FOUND: "No users in database.",
        }
    )
    def get(self):
        """
        Get all users.
        """
        try:
            users = UserManager.get_all()
        except ValidationError as error:
            api.abort(HTTPStatus.BAD_REQUEST, message=error.args[0])
        if not users:
            api.abort(
                HTTPStatus.NOT_FOUND,
                message="No users in database.",
            )
        return users
