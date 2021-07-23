"""Application HTTP

This module initializes the API and client for the application.

"""

from .api import init_api
from .client import init_client


def init_http(app):
    """
    Initialize HTTP.
    """
    init_api(app)
    init_client(app)
