from flask import request, render_template, redirect, url_for
from flask_login import login_user, logout_user, login_required
from apps.form.auth_forms import RegisterForm, LoginForm
from . import blog_bp
from apps.models.model import db, User


@blog_bp.route('/login/', methods=['GET', 'POST'], endpoint='login')
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            # 设置session
            login_user(user, remember=True)
            next_url = request.args.get('next') or '/'
            if not next_url.startswith('/'):
                next_url = '/'
            return redirect(next_url)
        form.password.errors = ['用户名或密码错误!']
    try:
        form.error = list(form.errors.values())[0][0]
    except:
        form.error = ''
    return render_template('blog/login.html', form=form)


@blog_bp.route('/register/', methods=['GET', 'POST'], endpoint='register')
def register():
    """注册"""
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User()
        user.set_attr(form.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('blog.login'))
    try:
        form.error = list(form.errors.values())[0][0]
    except:
        form.error = ''
    return render_template('blog/register.html', form=form)


@blog_bp.route('/logout')
@login_required
def logout():
    # 删除session
    logout_user()
    return redirect(url_for('blog.login'))
