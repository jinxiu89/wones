#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 18-4-26.
from . import main
from flask import render_template
from app.models.models import Article


@main.route("/article/details/<url_title>")
def article_details(url_title):
    article = Article.query.filter_by(url_title=url_title).first()
    return render_template('main/article/details.html', article=article)
