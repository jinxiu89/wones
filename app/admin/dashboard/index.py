#!/usr/bin/env python
# author:jinxiu89@163.com
# create by thomas on 18-1-27.
# from app.admin import admin
from app.admin import admin
from app.models.models import User
from flask import render_template, session, request
from app.decorate import admin_login


@admin.route("/")
@admin_login
def index():
    return render_template("/admin/dashboard.html")
