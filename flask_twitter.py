"""
    An extension for python twitter v2.
"""
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

        config = dict()
        for key, value in app.config.items():
            if key.startswith("TWITTER_"):
                config[key.lower().replace("twitter_", "")] = value

        return self.get_api(**config)

    @staticmethod
    def get_api(**kwargs):
        return Api(oauth_flow=True, **kwargs)
