#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 18-1-27.
from flask import Blueprint

main = Blueprint("main", __name__, url_prefix="/main")

from .errors import errors
from .index import index
from .article import lists, details
