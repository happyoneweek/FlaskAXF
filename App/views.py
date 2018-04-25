from flask_restful import Resource, fields, marshal_with, Api
from App.models import HomeBanner, HomeNav, HomeMustBuy, HomeShop

api = Api()


def init_api(app):
	api.init_app(app=app)


banner_fileds = {
	"img": fields.String,
	"name": fields.String,
	"trackid": fields.String,
}

nav_fields = {
	"img": fields.String,
	"name": fields.String,
	"trackid": fields.String,
}

mustbuy_fields = {
	"img": fields.String,
	"name": fields.String,
	"trackid": fields.String,
}

shop_fields = {
	"img": fields.String,
	"name": fields.String,
	"trackid": fields.String,
}


result_fileds = {
	"msg": fields.String,
	"status": fields.String,
	"banner_data": fields.List(fields.Nested(banner_fileds)),
	"nav_data": fields.List(fields.Nested(nav_fields)),
	"mustbuy_data": fields.List(fields.Nested(mustbuy_fields)),
	"shop_data": fields.List(fields.Nested(shop_fields)),


}


class HomeResource(Resource):

	@marshal_with(result_fileds)
	def get(self):
		homebanners = HomeBanner.query.all()
		homenav = HomeNav.query.all()
		homemustbuy = HomeMustBuy.query.all()
		homeshop = HomeShop.query.all()
		return {"msg": "ok", "banner_data": homebanners, "nav_data": homenav, "mustbuy_data": homemustbuy, "shop_data": homeshop}


api.add_resource(HomeResource, "/home/")
