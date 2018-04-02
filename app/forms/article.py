#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 18-3-22.
from app.forms import *


class ArticleForm(FlaskForm):
    category_id = SelectField(
        label="所属分类",
        coerce=int,
        validators={
            DataRequired("请选择分类"),
        },
        render_kw={
            "class": "select valid",
            "size": 1
        }
    )
    title = StringField(
        label="标题",
        description="文章标题",
        validators=[DataRequired("标题必须输入")],
        render_kw={
            "id": "title",
            "class": "input-text size-L",
            "placeholder": "标题"
        }
    )
    url_title = StringField(
        label="url标题",
        description="url标题",
        validators=[DataRequired("url标题必须输入")],
        render_kw={
            "id": "url_title",
            "class": "input-text size-L",
            "placeholder": "英文关键词为url title"
        }
    )
    keywords = StringField(
        label="关键词",
        description="文章关键词",
        render_kw={
            "id": "title",
            "class": "input-text size-L",
            "placeholder": "标题"
        }
    )
    description = TextAreaField(
        label="seo描述",
        description="seo描述",
        render_kw={
            "class": "textarea",
            "cols": "",
            "rows": "",
            "placeholder": "100字以内随便打",
            "dragonfly": "true",
        }
    )
    content = TextAreaField(
        label="正文",
        description="正文",
        render_kw={
            "class": "textarea",
            "rows": "",
            "cols": "",
            "placeholder": "100",
            "id": "editor"
        }
    )
    relationship = TextAreaField(
        label="相关文章",
        description="相关文章",
        render_kw={
            "class": "textarea",
            "rows": "",
            "cols": "",
            "placeholder": "",
            "id": "editor1",
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

    def __init__(self, *args, **kwargs):
        super(ArticleForm, self).__init__(*args, **kwargs)

    submit = SubmitField(render_kw={"class": "btn btn-success radius size-L", "value": "       保      存     "})
