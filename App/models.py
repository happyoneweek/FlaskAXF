from App.exts import db


class HomeBanner(db.Model):
    __tablename__='axf_wheel'
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    img=db.Column(db.String(200))
    name=db.Column(db.String(200))
    trackid=db.Column(db.String(16))
