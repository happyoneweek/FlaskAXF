from flask import Flask

from App import settings
from App.exts import init_ext
from App.urls import init_urls
from App.views import init_api


def create_app(env_name):
    app = Flask(__name__)
    app.config.from_object(settings.env.get(env_name))
    init_ext(app)
    init_api(app)
    init_urls(app)

    return app
