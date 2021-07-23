"""Database Intialization

This module initializes the database client and instances.

"""

from pymongo import MongoClient

from app.config import MONGO_CONNECTION, MONGO_USER, MONGO_PASSWORD

MONGO_CLIENT = MongoClient(
    MONGO_CONNECTION, username=MONGO_USER, password=MONGO_PASSWORD, authSource="profile"
)
