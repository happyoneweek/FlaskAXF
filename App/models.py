from App.exts import db


class HomeBanner(db.Model):
    __tablename__ = 'axf_wheel'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    img = db.Column(db.String(200))
    name = db.Column(db.String(200))
    trackid = db.Column(db.String(16))


class MainNav(db.Model):
    __tablename__ = 'axf_nav'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    img = db.Column(db.String(200))
    name = db.Column(db.String(100))
    trackid = db.Column(db.String(16))


class MainMustBuy(db.Model):
    __tablename__ = 'axf_mustbuy'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    img = db.Column(db.String(200))
    name = db.Column(db.String(100))
    trackid = db.Column(db.String(16))


class MainShop(db.Model):
    __tablename__ = 'axf_shop'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    img = db.Column(db.String(200))
    name = db.Column(db.String(100))
    trackid = db.Column(db.String(16))


class MainShow(db.Model):
    __tablename__ = 'axf_mainshow'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    img = db.Column(db.String(200))
    name = db.Column(db.String(100))
    trackid = db.Column(db.String(16))
    categoryid = db.Column(db.String(16))
    brandname = db.Column(db.String(100))
    img1 = db.Column(db.String(200))
    childcid1 = db.Column(db.String(16))
    productid1 = db.Column(db.String(200))
    longname1 = db.Column(db.String(100))
    price1 = db.Column(db.Float, default=0)
    marketprice1 = db.Column(db.Float, default=1)
    img2 = db.Column(db.String(200))
    childcid2 = db.Column(db.String(16))
    productid2 = db.Column(db.String(100))
    longname2 = db.Column(db.String(100))
    price2 = db.Column(db.Float, default=0)
    marketprice2 = db.Column(db.Float, default=1)
    img3 = db.Column(db.String(200))
    childcid3 = db.Column(db.String(16))
    productid3 = db.Column(db.String(16))
    longname3 = db.Column(db.String(200))
    price3 = db.Column(db.Float, default=0)
    marketprice3 = db.Column(db.Float, default=1)


class GoodType(db.Model):
    __tablename__ = 'axf_foodtypes'
    typeid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    typename = db.Column(db.String(200))
    childtypename = db.Column(db.String(200))
    typesort = db.Column(db.Integer, default=1)


class Goods(db.Model):
    __tablename__ = "axf_goods"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    productid = db.Column(db.String(16))
    productimg = db.Column(db.String(200))
    productname = db.Column(db.String(100))
    productlongname = db.Column(db.String(200))
    isxf = db.Column(db.Integer, default=1)
    pmdesc = db.Column(db.String(100))
    specifics = db.Column(db.String(100))
    price = db.Column(db.Float, default=0)
    marketprice = db.Column(db.Float, default=1)
    categoryid = db.Column(db.String(16))
    childcid = db.Column(db.String(16))
    childcidname = db.Column(db.String(100))
    dealerid = db.Column(db.Float, default=16)
    storenums = db.Column(db.Integer, default=1)
    productnum = db.Column(db.Integer, default=1)


class UserModel(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(32), unique=True)
    password = db.Column(db.String(256))
    email = db.Column(db.String(64), unique=True)
    sex = db.Column(db.Boolean(), default=False)
    icon = db.Column(db.String(256))
    is_delete = db.Column(db.Boolean(), default=False)


class CartModel(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user = db.Column(db.Integer, db.ForeignKey(UserModel.id))
    goods = db.Column(db.Integer, db.ForeignKey(Goods.id))
    c_num = db.Column(db.Integer, default=1)
    is_select = db.Column(db.Boolean, default=True)


class OrderModel(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user = db.Column(db.Integer, db.ForeignKey(UserModel.id))
    o_num = db.Column(db.String(64))
    o_status = db.Column(db.Integer, default=0)
    o_create = db.Column(db.DateTime, )


class OrderGoodsModel(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    goods = db.Column(db.Integer, db.ForeignKey(Goods.id))
    order = db.Column(db.Integer, db.ForeignKey(OrderModel.id))
    goods_num = db.Column(db.Integer, default=1)
