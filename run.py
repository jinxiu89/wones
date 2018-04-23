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


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


from app.filter import *

if __name__ == "__main__":
    app.run(host="0.0.0.0")
