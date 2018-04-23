#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 18-3-4.
from app.admin import admin
from flask import render_template, flash, redirect, request, session, url_for
from app.forms.login import LoginForm
from app.models.models import User


@admin.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        data = form.data
        query = User.query
        user = query.filter_by(name=data['name'])
        count = user.count()
        result = query.first()
        if count == 0:
            flash("用户不存在", "error")
        if not result.verify_password(data['password']):
            flash("密码不正确", "error")
            return redirect(url_for("admin.login"))
        if request.method == "POST":
            session['name'] = data['name']
            session['id'] = result.id
            return redirect(request.args.get("next") or url_for("admin.article"))
    return render_template("admin/login.html", form=form)
