# import os
#
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def get_db_uri(dbinfo):
    user = dbinfo.get("USER") or 'root'
    password = dbinfo.get("PASSWORD") or 'rock1204'
    host = dbinfo.get("HOST") or "localhost"
    port = dbinfo.get("PORT") or '3306'
    name = dbinfo.get("NAME") or 'mysql'
    db = dbinfo.get("DB") or 'mysql'
    driver = dbinfo.get("DRIVER") or 'pymysql'

    return "{}+{}://{}:{}@{}:{}/{}".format(db, driver, user, password, host, port, name)


class Config():
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "1234567890"
    SESSION_TYPE = "redis"


class DevelopConfig(Config):
    DEBUG = True

    DATABASE = {
        "USER": 'root',
        "PASSWORD": 'rock1204',
        "HOST": '39.106.174.160',
        "PORT": '3306',
        "NAME": 'FlaskDay06',
        'DB': 'mysql',
        'DRIVER': 'pymysql'
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


env = {
    "develop": DevelopConfig,
}
