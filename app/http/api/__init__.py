"""Application API

This module initializes the API for the application.

"""

from .profile import api_blueprint as profile_api
from .progress import api_blueprint as progress_api
from .communication import api_blueprint as communication_api


def init_api(app):
    """
    Initialize the API.
    """

    api_prefix = "/api"

    app.register_blueprint(profile_api, url_prefix="%s/profile" % api_prefix)
    app.register_blueprint(progress_api, url_prefix="%s/progress" % api_prefix)
    app.register_blueprint(
        communication_api, url_prefix="%s/communication" % api_prefix
    )
