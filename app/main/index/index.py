#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 18-1-27.
from . import main
from flask import render_template
from app.models.models import Article


@main.route("/")
def index():
    query = Article.query
    result = query.order_by(Article.update_time.desc()).all()
    count = query.count()

    return render_template("main/index/index.html", count=count, result=result)


@main.route("/login", methods=["GET", "POST"])
def login():
    return "login"
