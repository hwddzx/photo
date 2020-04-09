from flask_login import LoginManager
from apps.models.model import User

login_manager = LoginManager()

# 未登录状态跳转视图设置
login_manager.login_view = 'blog.login'
login_manager.login_message = '登录后才能访问'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

