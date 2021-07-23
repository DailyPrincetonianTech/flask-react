"""Profile Database Intialization

This module initializes the profile database instance.

"""

from umongo.frameworks import PyMongoInstance

from .. import MONGO_CLIENT

profile_db = PyMongoInstance(MONGO_CLIENT.profile)
