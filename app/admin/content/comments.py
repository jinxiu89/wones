#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 18-8-14.
from flask import flash, request, jsonify, session
from app.admin.content import *
from app.decorate import admin_login
from app.models.models import Reply


@admin.route("/content/comments")
@admin_login
def comments():
    query = Reply.query
    count = query.filter_by(is_show=2).count()
    result = query.filter_by(is_show=2).all()
    return render_template("admin/content/comments/index.html", count=count, result=result)


@admin.route("/content/comments/start/<int:id>", methods=["POST", "GET"])
@admin_login
def comments_start(id=None):
    result = Reply.query.get_or_404(id)
    result.is_show = 1
    Reply.action(result)
    return jsonify({"status": 1, "data": "成功"})


@admin.route("/content/comments/del/<int:id>", methods=["POST", "GET"])
@admin_login
def comments_del(id):
    result = Reply.query.get_or_404(id)
    Reply.delete(result)
    return jsonify({"status": 1, "data": "成功"})
