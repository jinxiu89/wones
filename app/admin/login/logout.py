#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 18-3-4.
from app.admin import admin
from flask import render_template, session, redirect, url_for, flash
from app.forms.login import LoginForm


@admin.route("/logout", methods=["GET", "POST"])
def logout():
    session.pop("name", None)
    session.pop("id", None)
    flash("成功退出！", "ok")
    return redirect(url_for("admin.login"))
