import os

from flask import url_for, app
from flask_admin.contrib.sqla import ModelView
from flask_admin import form
from jinja2 import Markup
from sqlalchemy.event import listens_for

from apps.models.model import User, Album, Category, Photo, Label

file_path = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")), 'static')


@listens_for(Photo, 'after_delete')
def del_image(mapper, connection, model_obj):
    if model_obj.img:
        try:
            os.remove(os.path.join(file_path, model_obj.img))
        except OSError:
            pass

        try:
            os.remove(os.path.join(
                file_path,
                form.thumbgen_filename(model_obj.img)))
        except OSError:
            pass


class PhotoModelView(ModelView):
    def _list_thumbnail(view, context, model, name):
        if not model.img:
            return ''

        return Markup('<img src="%s">' % url_for('static',
                                                 filename=form.thumbgen_filename(model.img)))

    column_formatters = {
        'img': _list_thumbnail
    }
    form_extra_fields = {
        'img': form.ImageUploadField('图片',
                                     base_path=file_path,
                                     relative_path='uploadFile/',
                                     thumbnail_size=(100, 100, True))
    }

    column_labels = {
        'id': '序号',
        'img': '图片',
        'img_url': '图片地址',
        'content': '详情',
        'album_id': '相册',
        'label_name': '标签',
        'created_time': '上传时间',
        'album': '相册',
        'album.title': '相册',
        'label': '标签',
        'is_delete': '是否删除',
    }
    column_list = ('id', 'img', 'content', 'album.title', 'label_name', 'created_time')

    def __init__(self, session, **kwargs):
        super(PhotoModelView, self).__init__(Photo, session, **kwargs)


class UserModelView(ModelView):
    can_create = False
    can_delete = False

    def _list_thumbnail(view, context, model, name):
        if not model.img:
            return ''

        return Markup('<img src="%s">' % url_for('static',
                                                 filename=form.thumbgen_filename(model.img)))

    column_formatters = {
        'img': _list_thumbnail
    }
    form_extra_fields = {
        'img': form.ImageUploadField('图片',
                                     base_path=file_path,
                                     relative_path='uploadFile/',
                                     thumbnail_size=(100, 100, True))
    }

    column_labels = {
        'id': '序号',
        'username': '用户名',
        'name': '姓名',
        'is_super_user': '管理员',
        'sex': '性别',
        'img': '头像',
        'is_delete': '是否删除',
        'album_of_user': '相册',
    }
    column_list = ('id', 'username', 'name', 'sex', 'img', 'is_super_user')

    def __init__(self, session, **kwargs):
        super(UserModelView, self).__init__(User, session, **kwargs)


class AlbumModelView(ModelView):
    # can_delete = False
    # 使列可搜索或用于筛选，请指定列名称列表
    column_searchable_list = ['title', 'username']
    column_filters = ['category_name']
    # 在列表视图中启用内嵌编辑
    # column_editable_list = ['title']
    # 让添加和编辑表单显示在列表页的模式窗口中，而不是专用的创建和编辑页面
    # create_modal = True
    # edit_modal = True
    column_labels = {
        'id': '序号',
        'title': '标题',
        'content': '内容详情',
        'created_time': '创建时间',
        'update_time': '更新时间',
        'user': '所属用户',
        'username': '用户名',
        'category': '分类',
        'is_delete': '是否删除',
        'photo': '照片',
        'category_name': '分类',
    }
    column_list = ('id', 'title', 'category', 'user', 'update_time',)

    def __init__(self, session, **kwargs):
        super(AlbumModelView, self).__init__(Album, session, **kwargs)


class CategoryModelView(ModelView):
    column_labels = {
        'id': '序号',
        'name': '名称',
        'is_delete': '是否删除',
        'album_of_category': '相册',
    }
    column_list = ('id', 'name')

    def __init__(self, session, **kwargs):
        super(CategoryModelView, self).__init__(Category, session, **kwargs)


class LabelModelView(ModelView):
    column_labels = {
        'id': '序号',
        'name': '名称',
        'colour': '颜色',
        'is_delete': '是否删除',
        'photo_of_label': '照片',
    }
    column_list = ('id', 'name', 'colour')

    def __init__(self, session, **kwargs):
        super(LabelModelView, self).__init__(Label, session, **kwargs)
