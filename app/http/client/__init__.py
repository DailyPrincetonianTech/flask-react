# pylint: disable = unused-argument

"""Application Client

This module points client requests to the React.js application build/ folder.

"""

import os
from flask import send_from_directory


def init_client(app):
    """
    Initialize the client.
    """

    @app.route("/", defaults={"path": ""})
    @app.route("/<path:path>")
    def serve(path):
        if path != "" and os.path.exists(app.static_folder + "/" + path):
            return send_from_directory(app.static_folder, path)
        return send_from_directory(app.static_folder, "index.html")

    @app.errorhandler(404)
    def not_found(error):
        return app.send_static_file("index.html")
