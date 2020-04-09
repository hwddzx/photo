from flask import request, render_template, redirect, url_for, jsonify
from flask_login import login_required, current_user
from . import blog_bp
from apps.models.model import db, Photo


@blog_bp.route('/', endpoint='index', methods=['GET', 'POST'])
@login_required
def index():
    if request.method == 'GET':
        if current_user.is_authenticated:
            pass
        photos = db.session.query(Photo).order_by(Photo.created_time.desc()).filter_by(is_delete=False)
        return render_template('blog/index.html', photos=photos)
    return jsonify({'code': 0, 'msg': '上传成功'})


@blog_bp.route('/category', endpoint='category', methods=['GET'])
@login_required
def category():
    return render_template('blog/category.html')


@blog_bp.route('/single', endpoint='single', methods=['GET'])
@login_required
def single():
    return render_template('blog/single.html')


@blog_bp.route('/about', endpoint='about', methods=['GET'])
@login_required
def about():
    return render_template('blog/about.html')


@blog_bp.route('/contact', endpoint='contact', methods=['GET'])
@login_required
def contact():
    return render_template('blog/contact.html')
