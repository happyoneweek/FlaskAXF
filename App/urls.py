from flask_restful import Api

from App.views import HomeResource, User

api = Api()

api.add_resource(HomeResource,"/home/")
api.add_resource(User, "/user/")
def init_urls(app):
    api.init_app(app=app)

