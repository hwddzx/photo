from wtforms import Form, StringField, PasswordField, validators
from apps.models.model import User, db


class LoginForm(Form):
    """登录form"""
    username = StringField(
        validators=[
            validators.DataRequired(message='请输入账号'),
            validators.Length(min=3, message='账号少于6个字符'),
            validators.Length(max=18, message='账号超出18个字符'),
        ],
    )

    password = PasswordField(
        validators=[
            validators.DataRequired(message='请输入密码'),
            validators.Length(min=6, message='密码少于6个字符'),
            validators.Length(max=18, message='密码超出18个字符'),
        ],
    )


class RegisterForm(LoginForm):
    """注册form,继承了登录form"""
    name = StringField(
        validators=[
            validators.DataRequired(message='请输入用户名'),
            validators.Length(min=2, message='用户名至少需要2个字符'),
            validators.Length(max=16, message='用户名最多设置16个字符')
        ]
    )
    repassword = PasswordField(
        validators=[
            validators.DataRequired(message='请再次输入密码'),
            validators.EqualTo('password', message='两次密码不一致')
        ],
    )

    def validate_username(self, field):
        # 验证用户名是否存在
        print(field.data)
        if db.session.query(User).filter_by(username=field.data).first():
            raise validators.ValidationError(message='用户名已存在')
