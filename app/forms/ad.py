#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 18-4-28.
from app.forms import *
from app.models.models import Ad
from db_exts import db
from flask import session
from utils import upload_image
from datetime import datetime


class AdForm(FlaskForm):
    name = StringField(label="广告名称",
                       description="广告名称",
                       render_kw={"id": "name",
                                  "class": "input-text size-L",
                                  "placeholder": "广告名称"
                                  })
    image = StringField(label="图片地址",
                        description='图片地址',
                        render_kw={"class": "btn btn-default",
                                   "style": "height:37px"})
    path = StringField(label="指向路径",
                       description="指向路径",
                       render_kw={"id": "path",
                                  "class": "input-text size-L",
                                  "placeholder": "http://"})
    status = SelectField(label="状态",
                         validators={DataRequired("必须选择一个")},
                         coerce=int,
                         choices=[(1, '启用'), (2, '禁用')],
                         render_kw={"class": "select valid",
                                    "size": 1})
    submit = SubmitField(render_kw={"class": "btn btn-success radius size-L", "value": "       保      存     "})
