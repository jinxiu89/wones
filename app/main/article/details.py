#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 18-4-26.
from . import main
from flask import render_template
from app.models.models import Article
from db_exts import db


@main.route("/article/details/<int:id>")
def article_details(id):
    article = Article.query.filter_by(id=id).first_or_404()
    if article.count is None:
        article.count = 1
    article.count = article.count + 1
    db.session.add(article)
    db.session.commit()
    return render_template('main/article/details.html', article=article)