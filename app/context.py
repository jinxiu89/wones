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
    输入热门王文章
    :return:
    """
    from app.models.models import Article
    hot_article = Article.query.filter(Article.count > 5).order_by(Article.count.desc()).limit(5).all()
    return dict(hot_article=hot_article)


@app.context_processor
def top():
    """
    输入好文推荐
    :return:
    """
    from app.models.models import Article
    top_article = Article.query.filter(Article.top == 1).order_by(Article.id.desc()).limit(5).all()
    return dict(top_article=top_article)


@app.context_processor
def friend():
    from app.models.models import Friends
    friends = Friends.query.filter(Friends.is_show == 1).order_by(Friends.id.desc()).all()
    return dict(friends=friends)


@app.context_processor
def copy_right():
    return dict(copy_right=datetime.datetime.now().year)
