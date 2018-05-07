#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 18-3-4.
from manager import app


# 获取文章分类名
@app.template_filter("getCategory")
def get_category(id):
    from app.models.models import Category
    category = Category.query.filter_by(id=int(id)).first_or_404()
    return category.name


@app.template_filter("getUser")
def get_user(id):
    from app.models.models import User
    return User.query.filter_by(id=int(id)).first_or_404().description


@app.template_filter("cutTitle")
def cut_str(string):
    return string[0:18]


@app.template_filter("cutDes")
def cut_des(string):
    return string[0:32] + "..."
