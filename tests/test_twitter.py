from flask_twitter import TwitterAPIV2


def test_init_app_oauth1(app):
    app.config = {
        "TWITTER_CONSUMER_KEY": "consumer key",
        "TWITTER_CONSUMER_SECRET": "consumer secret",
    }
    twitter = TwitterAPIV2(app).get_api()
    assert twitter.consumer_key == "consumer key"


def test_init_app_oauth2(app):
    app.config = {
        "TWITTER_CLIENT_ID": "client id",
    }
    twitter = TwitterAPIV2(app).get_api()
    assert twitter.client_id == "client id"
