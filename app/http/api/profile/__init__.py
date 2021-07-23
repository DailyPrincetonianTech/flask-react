"""Profile API

    This API namespace defines CRUD operations for profile models.

    Endpoints
    ----------
    /api/profile/<model> : GET
        Get <model> by ID.
    /api/profile/<model> : PUT
        Create <model> with JSON object.
    /api/profile/<model> : PATCH
        Update <model> by ID with JSON-encoded key-value pairs.
    /api/profile/<model> : DELETE
        Delete <model> by ID.
    /api/profile/<model>/all : GET
        Get all <models>.

"""

from flask import Blueprint
from flask_restx import Api

from .user import api as user_api


api_blueprint = Blueprint("api/profile/", __name__)
api = Api(
    api_blueprint,
    title="Profile API",
    version="0.3.0",
    description="Defines operations for profile models.",
)

api.add_namespace(user_api)
