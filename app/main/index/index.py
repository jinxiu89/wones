#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 18-1-27.
from . import main
from flask import render_template
from app.models.models import Article, Banner


@main.route("/")
def index():
    query = Article.query
    result = query.order_by(Article.id.desc()).all()
    banner = Banner.query.order_by(Banner.id).all()
    return render_template("main/index/index.html", result=result, banner=banner)


@main.route("/login", methods=["GET", "POST"])
def login():
    return "login"
