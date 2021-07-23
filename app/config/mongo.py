"""MongoDB Configuration"""

import os

MONGO_CONNECTION = os.environ.get("ORMONGO_RS_URL")
MONGO_USER = os.environ.get("MONGO_USER")
MONGO_PASSWORD = os.environ.get("MONGO_PASSWORD")
