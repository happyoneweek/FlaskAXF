from flask_restful import Resource, fields, marshal_with
from App.models import HomeBanner, GoodType

banner_fileds = {
    "img": fields.String,
    "name": fields.String,
    "trackid": fields.String
}


result_fileds = {
    "msg": fields.String,
    "status": fields.String,
    "banner_data": fields.List(fields.Nested(banner_fileds))
}


class HomeResource(Resource):

    @marshal_with(result_fileds)
    def get(self):
        homebanners = HomeBanner.query.all()
        return {"msg": "ok", "banner_data": homebanners}


class MarketResource(Resource):
    def get(self):
        goodtypes=GoodType.query.all()
        return {'msg':'ok'}

