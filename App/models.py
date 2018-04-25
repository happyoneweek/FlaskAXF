from App.exts import db


class HomeBanner(db.Model):
	__tablename__ = "axf_wheel"
	id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	img = db.Column(db.String(200))
	name = db.Column(db.String(200))
	trackid = db.Column(db.String(16))


'''
axf_nav(img,name,trackid)
'''


class HomeNav(db.Model):
	__tablename__ = 'axf_nav'
	img = db.Column(db.String(200))
	name = db.Column(db.String(200))
	trackid = db.Column(db.String(16))


"""
axf_mustbuy(img,name,trackid)
"""


class HomeMustBuy(db.Model):
	__tablename__ = 'axf_mustbuy'
	img = db.Column(db.String(200))
	name = db.Column(db.String(200))
	trackid = db.Column(db.String(16))


"""
axf_shop(img,name,trackid)
"""


class HomeShop(db.Model):
	__tablename__ = 'axf_shop'
	img = db.Column(db.String(200))
	name = db.Column(db.String(200))
	trackid = db.Column(db.String(16))






