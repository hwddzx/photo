import os


def get_db_dir():
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return 'sqlite:///{}/blog/blog.db'.format(path)


class BaseSettings(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = '18380433380'
    JSON_AS_ASCII = False
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:1234@127.0.0.1:3306/elm'
    SQLALCHEMY_DATABASE_URI = get_db_dir()
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BABEL_DEFAULT_LOCALE = 'zh_CN'
    FLASK_ADMIN_SWATCH = 'cerulean'


class DevelopmentSettings(BaseSettings):
    DEBUG = True


class TestSettings(BaseSettings):
    TESTING = True


class ProductionSettings(BaseSettings):
    pass
