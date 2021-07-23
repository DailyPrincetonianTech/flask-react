"""API Security Utilities"""

from http import HTTPStatus

from flask import request


def csrf_protection(function):
    """Require that the X-Requested-With header is present."""

    def protected(*args):
        if "X-Requested-With" in request.headers:
            return function(*args)
        return "X-Requested-With header missing", HTTPStatus.FORBIDDEN

    return protected
