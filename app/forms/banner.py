#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 18-3-22.
from app.forms import *
from app.models.models import Banner
from db_exts import db
from utils import upload_image
from flask import session
from datetime import datetime


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
            "class": "btn btn-default",
            "style": "height:37px"
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
            "size": 1,
            "style": "height:30px"
        }

    )

    submit = SubmitField(render_kw={"class": "btn btn-success radius size-L", "value": "       保      存     "})

    def create(self):
        banner = Banner(
            user_id=session.get("id"),
            title=self.title.data,
            image=upload_image(self.image.data),
            url=self.url.data,
            status=self.status.data
        )
        db.session.add(banner)
        db.session.commit()
        return banner

    def edit(self, banner):
        banner.user_id = session.get("id")
        banner.title = self.title.data
        banner.image = upload_image(self.image.data)
        banner.url = self.url.data
        banner.status = self.status.data
        banner.update_time = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        db.session.add(banner)
        db.session.commit()
        return banner
