#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 18-4-26.
from . import main
from app.models.models import Category, Article
from flask import render_template


@main.route("/article/list/<name>")
def article_lists(name):
    parent = Category.query.filter_by(name=name).first_or_404()
    article = parent.Article
    return render_template('main/article/lists.html', article=article, parent=parent)
