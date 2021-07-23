"""Flask-RestX Configuration"""

from datetime import datetime
from json import JSONEncoder


class CustomJSONEncoder(JSONEncoder):
    """Custom encoder for handling default values from a function call."""

    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()
        try:
            return super().default(o)
        except TypeError:
            return o.__dict__


RESTX_JSON = {"cls": CustomJSONEncoder}
