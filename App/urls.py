from flask_restful import Api

from App.views import HomeResource

api = Api()

api.add_resource(HomeResource,"/home/")

def init_urls(app):
    api.init_app(app=app)