# pylint: disable = no-member, protected-access

"""User Manager

This module defines the UserManager which allows
the API endpoints to interface with the database.

"""

from typing import List
from bson import ObjectId

from . import User


class UserManager:
    """
    User Manager
    """

    @staticmethod
    def get(_id: ObjectId) -> User:
        """
        Get user by ID.
        """
        return User.find_one({"_id": _id})

    @staticmethod
    def get_all() -> List[User]:
        """
        Get all users.
        """
        return User.find({})

    @staticmethod
    def create(user) -> User:
        """
        Create user with User object (NewUserSchema).
        """
        User.ensure_indexes()
        user.commit()
        return UserManager.get(user._id)

    @staticmethod
    def update(_id: ObjectId, updates) -> User:
        """
        Update user with User object (UserUpdateSchema).
        """
        user = UserManager.get(_id)
        user.update(updates)
        User.ensure_indexes()
        user.commit()
        return UserManager.get(_id)

    @staticmethod
    def delete(_id: ObjectId) -> User:
        """
        Delete user by ID.
        """
        user = UserManager.get(_id)

        user.delete()
        return user

    @staticmethod
    def query(query) -> User:
        """
        Query user by MongoDB query.
        """
        return User.find_one(query)

    @staticmethod
    def query_all(query) -> List[User]:
        """
        Query all users by MongoDB query.
        """
        return User.find(query)
