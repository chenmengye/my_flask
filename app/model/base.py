# @time: 2022-10-18 15:26
# @author: 39295
from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy


class SQLAlchemy(_SQLAlchemy):
    def auto_commit(self, throw=True):
        try:
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            if throw:
                raise e


db = SQLAlchemy()


class Base(db.Model):
    __abstract__ = True

    def set_attrs(self, attrs_dict):
        for key, value in attrs_dict.items():
            if hasattr(self, key):
                setattr(self, key, value)
