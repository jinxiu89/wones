#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 18-3-22.
from flask import flash, request, jsonify, session
from app.admin.content import *
from app.decorate import admin_login
from app.forms.banner import BannerForm
from app.models.models import Banner
from utils import upload_image


@admin.route("/content/banner")
@admin_login
def banner():
    query = Banner.query
    count = query.count()
    result = query.all()
    return render_template("admin/content/banner/banner.html", count=count, banner=result)


@admin.route("/content/banner/add", methods=["GET", "POST"])
def banner_add():
    form = BannerForm()
    if request.method == "POST":
        if form.validate_on_submit():
            form.create()
            flash("保存成功", "ok")
    return render_template("admin/content/banner/banner_add.html", form=form)


@admin.route("/content/banner/edit/<int:id>", methods=['GET', 'POST'])
def banner_edit(id=None):
    if id is None:
        result = {
            "status": 0,
            "data": "没有数据"
        }
        return jsonify(result)
    form = BannerForm()
    result = Banner.query.get_or_404(id)
    if request.method == "GET":
        form.status.data = result.status
    if request.method == "POST":
        if form.validate_on_submit():
            form.edit(result)
            flash("保存成功", "ok")
    return render_template("admin/content/banner/banner_edit.html", form=form, result=result)

