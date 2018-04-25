#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 18-1-27.
from flask import Blueprint

main = Blueprint("main", __name__, url_prefix="/")

from .index import index
from .errors import errors
