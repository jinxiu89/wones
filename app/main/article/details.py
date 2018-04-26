#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 18-4-26.
from . import main
from flask import render_template
from app.models.models import Article


@main.route("/article/details/<int:id>")
def article_details(id):
    article = Article.query.get_or_404(id)
    return render_template('main/article/details.html', article=article)
