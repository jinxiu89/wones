#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 18-4-24.
from manager import app


@app.context_processor
def navbar():
    from app.models.models import Category
    category = Category.query.all()
    return dict(category=category)


@app.context_processor
def hot():
    from app.models.models import Article
    hot_article = Article.query.limit(5).all()
    return dict(hot_article=hot_article)
