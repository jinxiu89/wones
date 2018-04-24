#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 18-4-24.
from manager import app


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
    输入热门王文章
    :return:
    """
    from app.models.models import Article
    hot_article = Article.query.limit(5).all()
    return dict(hot_article=hot_article)
