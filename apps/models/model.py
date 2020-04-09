from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from apps.models import BaseModel, db
from sqlalchemy.ext.declarative import declarative_base


class User(BaseModel, UserMixin):
    __table_name__ = 'user'
    username = db.Column(db.String(16), unique=True, index=True)
    name = db.Column(db.String(16), unique=True, index=True)
    _password = db.Column('password', db.String(128), nullable=False)
    is_super_user = db.Column(db.Boolean, default=False)
    sex = db.Column(db.String(2), default='男')
    img = db.Column(db.String(128), default='images/morentouxiang.jpeg')
    age = db.Column(db.SmallInteger, default=0)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, val):
        self._password = generate_password_hash(val)

    def check_password(self, user_pwd):
        return check_password_hash(self._password, user_pwd)

    def __repr__(self):
        return self.name

    __table_args__ = {
        # db.UniqueConstraint('id', 'name', name='uix_id_name'),
        # db.Index('ix_id_name', 'name', 'email'),
        # 指定表的引擎和字符编码
        'mysql_charset': 'utf8',
        'mysql_engine': 'InnoDB',

    }


class Album(BaseModel):
    """相册"""
    title = db.Column(db.String(32), unique=True, index=True)
    content = db.Column(db.Text())
    created_time = db.Column(db.DateTime, default=datetime.now)
    update_time = db.Column(db.DateTime, onupdate=datetime.now)

    username = db.Column(db.ForeignKey('user.username'))
    user = db.relationship('User', backref='album_of_user')

    category_name = db.Column(db.ForeignKey('category.name'))
    category = db.relationship('Category', backref='album_of_category')

    def __repr__(self):
        return self.title


class Photo(BaseModel):
    title = db.Column(db.String(32), unique=True, index=True)
    img = db.Column(db.String(128))
    content = db.Column(db.Text())

    album_id = db.Column(db.ForeignKey('album.id'))
    album = db.relationship('Album', backref='photo')

    label_name = db.Column(db.ForeignKey('label.name'))
    label = db.relationship('Label', backref='photo_of_label')

    created_time = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return self.img


class Category(BaseModel):
    name = db.Column(db.String(12))

    def __repr__(self):
        return self.name


class Label(BaseModel):
    name = db.Column(db.String(12))
    colour = db.Column(db.String(24))

    def __str__(self):
        return self.name
