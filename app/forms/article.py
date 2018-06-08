#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 18-3-22.
from app.forms import *
from app.models.models import Article
from db_exts import db
from flask import session
from utils import upload_image, del_image
from datetime import datetime


class ArticleForm(FlaskForm):
    category_id = SelectField(
        label="所属分类",
        coerce=int,
        validators={
            DataRequired("请选择分类"),
        },
        render_kw={
            "class": "select valid",
            "size": 1,
            "style": "height:30px",
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
    image = FileField(
        label="上传图片",
        validators=[],
        render_kw={
            "class": "btn btn-default",
            "style": "height:37px"
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
    markdown = TextAreaField(
        label="markdown",
        description="markdown"

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

    def create(self):
        article = Article(
            user_id=session.get("id"),
            category_id=self.category_id.data,
            title=self.title.data,
            url_title=self.url_title.data,
            keywords=self.keywords.data,
            description=self.description.data,
            image=upload_image(self.image.data),
            content=self.content.data,
            markdown=self.markdown.data,
            relationship=self.relationship.data,
            status=self.status.data,
        )
        db.session.add(article)
        db.session.commit()
        return article

    def edit(self, article):
        article.user_id = session.get("id")
        article.category_id = self.category_id.data
        article.title = self.title.data
        article.url_title = self.url_title.data
        article.keywords = self.keywords.data
        article.description = self.description.data
        if self.image.data:
            if article.image is not None:
                del_image(article.image)
            article.image = upload_image(self.image.data)
        article.content = self.content.data
        article.markdown = self.markdown.data
        article.relationship = self.relationship.data
        article.update_time = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        article.status = self.status.data
        db.session.add(article)
        db.session.commit()
        return article
