from flask import Flask
from flask_admin import Admin
from flask_babelex import Babel

from apps.admin.views import UserModelView, AlbumModelView, CategoryModelView, LabelModelView, PhotoModelView
from apps.blog import blog_bp
from apps.models import db
from apps.tools.login_tools import login_manager

app = Flask(__name__, template_folder='templates', static_folder='static')

admin = Admin(app, name='相册后台管理', template_mode='bootstrap3')

Babel(app)

# 配置文件
app.config.from_object('settings.DevelopmentSettings')
# 注册蓝图
app.register_blueprint(blog_bp)
# 注册模型
db.init_app(app)
# 登陆管理
login_manager.init_app(app)

# 注册admin model
admin.add_view(AlbumModelView(db.session, name='相册管理', category='相册'))
admin.add_view(PhotoModelView(db.session, name='照片管理', category='相册'))
admin.add_view(UserModelView(db.session, name='用户管理', category='用户'))
admin.add_view(CategoryModelView(db.session, name='分类管理', category='设置'))
admin.add_view(LabelModelView(db.session, name='标签管理', category='设置'))
