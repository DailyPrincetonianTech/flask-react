# pylint: disable = no-member, too-few-public-methods, abstract-method

"""User Model/Schema

This module contains the User model/schema definitions + schemas for
new users and user updates.

"""

from datetime import datetime
from bson import ObjectId

from umongo import Document, fields, RemoveMissingSchema
from flask_login import UserMixin

from app.db.profile import profile_db


@profile_db.register
class User(Document, UserMixin):
    """
    User Model
    """

    MA_BASE_SCHEMA_CLS = RemoveMissingSchema

    REQUIRED_ON_CREATE = ["name", "email", "phone", "profile_pic"]
    READ_ONLY = ["_id", "joined"]

    _id = fields.ObjectIdField(default=ObjectId())
    joined = fields.DateTimeField(default=datetime.now())

    name = fields.StringField(required=True)
    email = fields.EmailField(unique=True, required=True)
    phone = fields.StringField(unique=True, required=True)
    profile_pic = fields.UrlField(required=True)

    class Meta:
        """
        Meta ==> Collection reference.
        """

        collection_name = "users"

    def get_id(self):
        return self._id


class UserSchema(User.schema.as_marshmallow_schema()):
    """
    User Schema
    """

    class Meta:
        """
        Meta ==> Read-only fields fields.
        """

        dump_only = User.READ_ONLY
