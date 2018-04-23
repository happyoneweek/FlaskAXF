from flask_restful import Api

from App.views import Hello

api = Api()

api.add_resource(Hello,"/hello/")

def init_urls(app):
    api.init_app(app=app)