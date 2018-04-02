#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 18-3-22.
from app.admin.content import *
from app.models.models import Category, Article,User
from app.forms.article import ArticleForm
from werkzeug.security import generate_password_hash
from db_exts import db
from flask import flash, request, jsonify, session
from app.decorate import admin_login


@admin.route("/content/article")
@admin_login
def article():
    query = Article.query
    count = query.count()
    result = query.all()
    return render_template("admin/content/article/article.html", count=count, article=result)


@admin.route("/content/article/add", methods=["GET", "POST"])
def article_add():
    form = ArticleForm()
    category = Category.query.all()
    category = [(i.id, i.name) for i in category]
    if not category:
        category.insert(0, (1, "根分类"))
    form.category_id.choices = category
    if request.method == "POST":
        if form.validate_on_submit():
            data = form.data
            result = Article(
                user_id=int(session.get('id')),
                category_id=data['category_id'],
                title=data['title'],
                url_title=data['url_title'],
                keywords=data['keywords'],
                description=data['description'],
                content=data['content'],
                relationship=data['relationship'],
                status=data['status']
            )
            db.session.add(result)
            db.session.commit()
            flash("保存成功", "ok")
    return render_template("admin/content/article/article_add.html", form=form)
