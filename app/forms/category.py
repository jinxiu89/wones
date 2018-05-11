#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 18-3-19.
from app.forms import *


class CategoryForm(FlaskForm):
    name = StringField(
        label="分类名",
        validators=[DataRequired("请输入分类名")],
        description="category",
        render_kw={
            "class": "input-text",
            "placeholder": "请输入分类名，例如：Python",
            "id": "category",
        }
    )
    keywords = StringField(
        label="关键词",
        validators=[DataRequired("请输入分类关键词")],
        description="category",
        render_kw={
            "class": "input-text",
            "placeholder": "请输入分类关键词，例如：Python",
            "id": "keywords",
        }
    )
    image = FileField(
        label="电脑端图片",
        validators=[DataRequired("请上传图片")],
        render_kw={
            "class": "btn btn-default",
            "style": "height:37px"
        }
    )
    smallimage = FileField(
        label="手机端图片",
        validators=[DataRequired("请上传图片")],
        render_kw={
            "class": "btn btn-default",
            "style": "height:37px"
        }
    )
    description = StringField(
        label="描述",
        validators=[DataRequired("请输入描述")],
        description="关键词描述",
        render_kw={
            "class": "input-text",
            "placeholder": "请输入分类描述，例如：Python",
            "id": "description",
        }
    )
    submit = SubmitField(render_kw={"class": "btn btn-primary radius", "value": "保存提交"})
