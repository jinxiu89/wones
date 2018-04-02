#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 18-3-18.
# 第一条：导入system包里的几条import
# 第二条：导入模型数据
# 第三条：导入表单数据
from app.admin.system import *
from app.models.models import User
from app.forms.user import UserForm
from werkzeug.security import generate_password_hash
from db_exts import db
from flask import flash, request, jsonify


# 用户列表
@admin.route("/system/user")
def system_user():
    query = User.query
    result = query.all()
    count = query.count()
    return render_template("admin/system/user/manger.html", result=result, count=count)


# 用户新增
@admin.route("/system/user/add", methods=['POST', 'GET'])
def system_user_add():
    form = UserForm()
    if form.validate_on_submit():
        data = form.data
        data = User(
            name=data['name'],
            password=generate_password_hash(data['password']),
            description=data['description'],
            is_admin=data['is_admin'],
            image=""
        )
        db.session.add(data)
        db.session.commit()
        flash("新增成功", "ok")
    return render_template("admin/system/user/user_add.html", form=form)


@admin.route("/system/user/edit/<int:id>", methods=["POST", "GET"])
def system_user_edit(id=None):
    if id is None or not id:
        pass
    form = UserForm()
    result = User.query.get_or_404(id)
    if request.method == "GET":
        form.description.data = result.description
        form.is_admin.data = result.is_admin
    if request.method == "POST":
        if form.validate_on_submit():
            data = form.data
            result.name = data['name']
            result.password = generate_password_hash(data['password'])
            result.description = data['description']
            result.is_admin = data['is_admin']
            db.session.add(result)
            db.session.commit()
            flash("保存成功", "ok")
    return render_template("admin/system/user/user_edit.html", form=form, result=result)
