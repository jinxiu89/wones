#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 18-3-19.
from app.admin.system import *
from app.models.models import Category
from app.forms.category import CategoryForm
from werkzeug.security import generate_password_hash
from db_exts import db
from flask import flash, request, jsonify
from app.decorate import admin_login


@admin.route("/system/category")
@admin_login
def system_category():
    query = Category.query
    result = query.all()
    count = query.count()
    return render_template("admin/system/category/category.html", result=result, count=count)


@admin.route("/system/category/add", methods=['POST', 'GET'])
@admin_login
def system_category_add():
    form = CategoryForm()
    if request.method == "POST":
        if form.validate_on_submit():
            data = form.data
            result = Category(
                name=data['name'],
                keywords=data['keywords'],
                description=data['description']
            )
            db.session.add(result)
            db.session.commit()
            flash("新增成功", "ok")
    return render_template("admin/system/category/category_add.html", form=form)


@admin.route("/system/category/edit/<int:id>", methods=['POST', 'GET'])
@admin_login
def system_category_edit(id=None):
    if id is None:
        result = {
            "status": 0,
            "data": "没有数据"
        }
        return jsonify(result)
    form = CategoryForm()
    result = Category.query.get_or_404(id)
    if request.method == "POST":
        if form.validate_on_submit():
            data = form.data
            result.name = data['name']
            result.keywords = data['keywords']
            result.description = data['description']
            db.session.add(result)
            db.session.commit()
            flash("保存成功", "ok")
    return render_template("admin/system/category/category_edit.html", form=form, result=result)
