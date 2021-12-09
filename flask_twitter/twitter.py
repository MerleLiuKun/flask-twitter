"""
    An extension for python twitter v2.
"""
from flask import current_app
from pytwitter import Api

DEFAULT_CONFIG = {
    "TWITTER_CALLBACK_URI": "https://localhost/",
    "TWITTER_SCOPES": ["users.read", "tweet.read"],
}


class TwitterAPIV2:
    def __init__(self, app=None):
        self.app = app
        if self.app is not None:
            self.init_app(app=app)

    def init_app(self, app):
        for key, value in DEFAULT_CONFIG.items():
            app.config.setdefault(key, value)

    @staticmethod
    def get_api():
        config = dict()
        for key, value in current_app.config.items():
            if key.startswith("TWITTER_"):
                config[key.lower().replace("twitter_", "")] = value
        return Api(oauth_flow=True, **config)
