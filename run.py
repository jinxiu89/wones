#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 18-4-21.
from werkzeug.contrib.fixers import ProxyFix
import app.models
from create_app import app
from db_exts import db

db.init_app(app)
db.app = app
app = app
from app.filter import *
from app.context import *


if __name__ == "__main__":
    app.wsgi_app = ProxyFix(app.wsgi_app)
    app.run()
