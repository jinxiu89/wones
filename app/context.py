#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 18-4-24.
from manager import app
import datetime


@app.context_processor
def navbar():
    """
    上下文，给base页面输出分类信息
    :return:
    """
    from app.models.models import Category
    category = Category.query.all()
    return dict(category=category)


@app.context_processor
def hot():
    """
    输入热门文章
    :return:
    """
    from app.models.models import Article
    hot_article = Article.query.filter(Article.count > 5).order_by(Article.count.desc()).limit(5).all()
    return dict(hot_article=hot_article)


@app.context_processor
def copy_right():
    return dict(copy_right=datetime.datetime.now().year)
