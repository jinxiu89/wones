#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 18-3-22.
from flask import flash, request, jsonify, session
from app.admin.content import *
from app.decorate import admin_login
from app.forms.article import ArticleForm
from app.models.models import Banner
from db_exts import db


@admin.route("/content/banner")
@admin_login
def banner():
    query = Banner.query
    count = query.count()
    result = query.all()
    return render_template("admin/content/banner/banner.html", count=count, article=result)


@admin.route("/content/banner/add", methods=["GET", "POST"])
def banner_add():
    form = ArticleForm()
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


@admin.route("/content/banner/edit/<int:id>", methods=['GET', 'POST'])
def banner_edit(id=None):
    if id is None:
        result = {
            "status": 0,
            "data": "没有数据"
        }
        return jsonify(result)
    form = ArticleForm()
    category = Category.query.all()
    category = [(i.id, i.name) for i in category]
    if not category:
        category.insert(0, (1, "根分类"))
    form.category_id.choices = category
    result = Article.query.get_or_404(id)
    if request.method == "GET":
        form.category_id.data = result.category_id
        form.description.data = result.description
        form.content.data = result.content
        form.relationship.data = result.relationship
        form.status.data = result.status
    if request.method == "POST":
        if form.validate_on_submit():
            data = form.data
            result.category_id = data['category_id']
            result.title = data['title']
            result.url_title = data['url_title']
            result.keywords = data['keywords']
            result.description = data['description']
            result.content = data['content']
            result.relationship = data['relationship']
            result.status = data['status']
            db.session.add(result)
            db.session.commit()
            flash("保存成功", "ok")
    return render_template("admin/content/article/article_edit.html", form=form, result=result)
