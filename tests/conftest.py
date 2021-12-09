import pytest
from flask import Flask


@pytest.fixture
def app():
    app = Flask(__name__)
    ctx = app.app_context()
    ctx.push()
    return app
