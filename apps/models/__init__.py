from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class BaseModel(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    is_delete = db.Column(db.Boolean, default=False)

    # 定义从attrs字典结构中,赋值表字段名称
    def set_attr(self, form_data: dict):
        for k, v in form_data.items():
            if hasattr(self, k) and k != 'id':
                setattr(self, k, v)

    def __getitem__(self, item):
        if hasattr(self, item):
            return getattr(self, item)


from . import model
