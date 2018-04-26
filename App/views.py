import hashlib

from flask import request, jsonify
from flask_restful import Resource, fields, marshal_with

from App.exts import db
from App.models import HomeBanner, GoodType, UserModel

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


class MarketResource(Resource):
    def get(self):
        goodtypes=GoodType.query.all()
        return {'msg':'ok'}

usermodel_fields = {
      "id":fields.Integer,
      "usernamev":fields.String,
      "password":fields.String,
      "email":fields.String,
      "sex":fields.Boolean(default=False),
      "icon":fields.String,
      "is_delete":fields.Boolean(default=False)
}
user_fields = {
    "msg":fields.String(default="ok"),
    "status":fields.String(default="200"),
    "data":fields.Nested(usermodel_fields)
}



class User(Resource):
    @marshal_with(user_fields)
    def get(self):
        pass
    def post(self):
        username = request.form.get("username")
        password = request.form.get("password")
        email = request.form.get("email")
        icon = request.form.get("icon")
        data = {
            "msg": "ok",
            "status": "422"
        }
        if not username or not password:
            data["msg"] = "參數不正確"
            return jsonify(data), 422

        user = UserModel()
        user.username = username
        user.password = generate_password(password)
        user.email = email
        user.icon = icon
        try:
            db.session.add(user)
            db.session.commit()
            data["status"] = "201"
        except Exception as e:
            data["status"] = "901"
            data["msg"] = str(e)
        return jsonify(data), 201

    def patch(self):
        pass
    def delete(self):
        pass



def generate_password(password):

    sha = hashlib.sha512()

    sha.update(password.encode("utf-8"))

    return sha.hexdigest()












