#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 18-3-22.
from app.forms import *
from app.models.models import Banner
from db_exts import db
from utils import upload_image
from flask import session


class BannerForm(FlaskForm):
    title = StringField(
        label="标题",
        description="幻灯片标题",
        validators=[DataRequired("标题必须输入")],
        render_kw={
            "id": "title",
            "class": "input-text size-L",
            "placeholder": "标题"
        }
    )
    url = StringField(
        label="跳转地址",
        description="跳转地址",
        validators=[DataRequired("必须输入")],
        render_kw={
            "id": "url",
            "class": "input-text size-L",
            "placeholder": "http://www.baidu.com"
        }
    )
    image = FileField(
        label="上传图片",
        validators=[DataRequired("请上传图片")],
        render_kw={
            "class": "btn btn-default"
        }
    )
    status = SelectField(
        label="状态",
        validators={
            DataRequired("必须选择一个")
        },
        coerce=int,
        choices=[(1, '启用'), (2, '禁用')],
        render_kw={
            "class": "select valid",
            "size": 1
        }

    )

    submit = SubmitField(render_kw={"class": "btn btn-success radius size-L", "value": "       保      存     "})

    def create(self):
        banner = Banner()
        self.populate_obj(article)
        db.session.add(banner)
        db.session.commit()
        return banner

    def edit(self, banner):
        banner.image.data = upload_image(self.image.data)
        self.populate_obj(banner)
        db.session.add(banner)
        db.session.commit()
        return banner
