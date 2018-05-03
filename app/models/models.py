#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 18-1-27.
from app.models import *
from flask import current_app


class BaseModel(db.Model):
    __abstract__ = True
    create_time = db.Column(db.DateTime, default=datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"))
    update_time = db.Column(db.DateTime, default=datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"),
                            onupdate=datetime.utcnow())


class User(BaseModel):
    """
    用户表，超级用户可以发表文章，审核，评论
    """
    __tablename__ = "tb_user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)
    password = db.Column(db.String(255))
    join_time = db.Column(db.DateTime, default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    description = db.Column(db.Text)
    is_admin = db.Column(db.SmallInteger)
    image = db.Column(db.Text)
    article = db.relationship("Article", backref="user", lazy='dynamic')
    reply = db.relationship("Reply", backref="user", lazy='dynamic')
    banner = db.relationship("Banner", backref="user", lazy='dynamic')

    def __repr__(self):
        return '<name %r>' % self.name

    def verify_password(self, password):
        return check_password_hash(self.password, password)


class Category(BaseModel):
    """
    文章分类，每一篇文章都归为一类
    """
    __tablename__ = "tb_category"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    keywords = db.Column(db.String(32))
    description = db.Column(db.String(255))
    short = db.Column(db.Integer)
    create_time = db.Column(db.DateTime, default=datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"))
    Article = db.relationship("Article", backref="category", lazy='dynamic')

    def __repr__(self):
        return '<name %r>' % self.name


class Ad(BaseModel):
    __tablename__ = "tb_ad"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    image = db.Column(db.String(255))
    path = db.Column(db.Text)
    status = db.Column(db.SmallInteger)

    def __repr__(self):
        return '<name %r>' % self.name


class Article(BaseModel):
    """
    文章表，只有注册的用户才能发表文章，必须制定分类
    """
    __tablename__ = "tb_article"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("tb_user.id"))
    category_id = db.Column(db.Integer, db.ForeignKey("tb_category.id"))
    title = db.Column(db.String(64))
    url_title = db.Column(db.String(32))
    keywords = db.Column(db.String(32))
    description = db.Column(db.String(255))
    image = db.Column(db.String(255))
    content = db.Column(db.Text)
    relationship = db.Column(db.Text)
    status = db.Column(db.SmallInteger)
    reply = db.relationship("Reply", backref="article")
    count = db.Column(db.Integer, default=int(100))

    def __repr__(self):
        return '<title %r>' % self.title


class Banner(BaseModel):
    __tablename__ = "tb_banner"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("tb_user.id"))
    title = db.Column(db.String(64))
    image = db.Column(db.String(255))
    url = db.Column(db.String(255))
    status = db.Column(db.SmallInteger, default=int(1))

    def __repr__(self):
        return '<title %r>' % self.title

    @staticmethod
    def stop(banner):
        db.session.add(banner)
        if db.session.commit():
            return True

    @staticmethod
    def start(banner):
        db.session.add(banner)
        db.session.commit()
        return True

    def delete(banner):
        if banner.image and os.path.exists(current_app.config.get('IMG_DIR') + banner.image):
            os.remove(current_app.config.get('IMG_DIR') + banner.image)
        db.session.delete(banner)
        db.session.commit()
        return True


class Reply(BaseModel):
    """
    回复文章，和用户关联，必须注册后才能评论恢复文章！
    """
    __tablename__ = "tb_reply"
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey("tb_user.id"))
    article_id = db.Column(db.Integer, db.ForeignKey("tb_article.id"))
    reply_time = db.Column(db.DateTime, default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    is_show = db.Column(db.SmallInteger, default=int(2))

    def __repr__(self):
        return "<content %r>" % self.content


class Images(BaseModel):
    __tablename__ = "tb_images"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))
    image_path = db.Column(db.String(255))
    description = db.Column(db.String(128))

    def __repr__(self):
        return '<title %r>' % self.title
