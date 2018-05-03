#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 18-3-22.
from flask import flash, request, jsonify, session
from app.admin.content import *
from app.decorate import admin_login
from app.forms.article import ArticleForm
from app.models.models import Category, Article
from utils import del_image


@admin.route("/content/article")
@admin_login
def article():
    query = Article.query
    count = query.count()
    result = query.all()
    return render_template("admin/content/article/article.html", count=count, article=result)


@admin.route("/content/article/add", methods=["GET", "POST"])
@admin_login
def article_add():
    form = ArticleForm()
    category = Category.query.all()
    category = [(i.id, i.name) for i in category]
    if not category:
        category.insert(0, (1, "根分类"))
    form.category_id.choices = category
    if request.method == "POST":
        if form.validate_on_submit():
            form.create()
            flash("保存成功", "ok")
    return render_template("admin/content/article/article_add.html", form=form)


@admin.route("/content/article/edit/<int:id>", methods=['GET', 'POST'])
@admin_login
def article_edit(id=None):
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
            image = result.image
            if del_image(image) is True:
                if form.edit(result):
                    flash("保存成功", "ok")
                else:
                    flash("保存失败", "error")
            else:
                flash("图片删除错误", "error")
    return render_template("admin/content/article/article_edit.html", form=form, result=result)
