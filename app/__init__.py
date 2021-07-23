"""Connect UPskill v0.3.0

Let's democratize recruiting together.

Made w/ love. ==> @areeq-hasan, @mwad22, @tbegum, @tvu20
"""


from flask import Flask

from .http import init_http


def create_app():
    """
    Application Factory
    """
    app = Flask(__name__, static_url_path="", static_folder="../build")

    app.config.from_object("app.config")
    app.secret_key = app.config["SECRET_KEY"]

    init_http(app)

    return app
