#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 18-3-22.
from flask import flash, request, jsonify, session
from app.admin.content import *
from app.decorate import admin_login
from app.forms.ad import AdForm
from app.models.models import Ad
from utils import upload_image, del_image


@admin.route("/content/ad")
@admin_login
def ad():
    query = Ad.query
    count = query.count()
    result = query.all()
    print(count)
    return render_template("admin/content/ad/index.html", count=count, result=result)


@admin.route("/content/ad/add", methods=["GET", "POST"])
def ad_add():
    form = AdForm()
    if request.method == "POST":
        if form.validate_on_submit():
            form.create()
            flash("保存成功", "ok")
    return render_template("admin/content/ad/ad_add.html", form=form)


@admin.route("/content/ad/edit/<int:id>", methods=['GET', 'POST'])
def ad_edit(id=None):
    if id is None:
        result = {
            "status": 0,
            "data": "没有数据"
        }
        return jsonify(result)
    form = AdForm()
    result = Ad.query.get_or_404(id)
    if request.method == "GET":
        form.status.data = result.status
    if request.method == "POST":
        if form.validate_on_submit():
            form.edit(result)
            flash("保存成功", "ok")
    return render_template("admin/content/ad/ad_edit.html", form=form, result=result)


@admin.route("/content/ad/stop/<int:id>", methods=["POST", "GET"])
def ad_stop(id=None):
    result = Ad.query.get_or_404(id)
    result.status = 2
    Ad.action(result)
    return jsonify({"status": 1, "data": "禁用成功"})


@admin.route("/content/ad/start/<int:id>", methods=["GET", "POST"])
def ad_start(id=None):
    result = Ad.query.get_or_404(id)
    result.status = 1
    Ad.action(result)
    return jsonify({"status": 1, "data": "启用成功"})


@admin.route("/content/ad/del/<int:id>", methods=["GET", "POST"])
def ad_del(id=None):
    result = Ad.query.get_or_404(id)
    Ad.delete(result)
    return jsonify({"status": 1, "data": "成功"})
