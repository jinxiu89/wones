#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 18-1-27.
from . import main
from flask import render_template, request
from app.models.models import Article


@main.route("/")
def index():
    page = request.args.get("page", 1, type=int)
    query = Article.query
    result = query.order_by(Article.id.desc()).paginate(page, per_page=10, error_out=False)
    # banner = Banner.query.order_by(Banner.id).all()
    return render_template("main/index/index.html", result=result)


@main.route("/login", methods=["GET", "POST"])
def login():
    return "login"
