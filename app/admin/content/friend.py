#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 18-3-22.
from flask import flash, request, jsonify
from app.admin.content import *
from app.decorate import admin_login
from app.forms.friend import FriendForm
from app.models.models import Friends


@admin.route("/content/friend")
@admin_login
def friend():
    query = Friends.query
    count = query.count()
    result = query.all()
    return render_template("admin/content/friend/index.html", count=count, result=result)


@admin.route("/content/friend/add", methods=["GET", "POST"])
def friend_add():
    form = FriendForm()
    if request.method == "POST":
        if form.validate_on_submit():
            form.create()
            flash("保存成功", "ok")
    return render_template("admin/content/friend/friend_add.html", form=form)


@admin.route("/content/friend/edit/<int:id>", methods=['GET', 'POST'])
def friend_edit(id=None):
    if id is None:
        result = {
            "status": 0,
            "data": "没有数据"
        }
        return jsonify(result)
    form = FriendForm()
    result = Friends.query.get_or_404(id)
    if request.method == "GET":
        form.is_show.data = result.is_show
    if request.method == "POST":
        if form.validate_on_submit():
            form.edit(result)
            flash("保存成功", "ok")
    return render_template("admin/content/friend/friend_edit.html", form=form, result=result)


@admin.route("/content/friend/stop/<int:id>", methods=["POST", "GET"])
def friend_stop(id=None):
    result = Friends.query.get_or_404(id)
    result.is_show = 2
    Friends.stop(result)
    return jsonify({"status": 1, "data": "禁用成功"})


@admin.route("/content/friend/start/<int:id>", methods=["GET", "POST"])
def friend_start(id=None):
    result = Friends.query.get_or_404(id)
    result.is_show = 1
    Friends.start(result)
    return jsonify({"status": 1, "data": "启用成功"})


@admin.route("/content/friend/del/<int:id>", methods=["GET", "POST"])
def friend_del(id=None):
    result = Friends.query.get_or_404(id)
    Friends.delete(result)
    return jsonify({"status": 1, "data": "成功"})
