#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 18-3-7.
from app.forms import *


class LoginForm(FlaskForm):
    name = StringField(
        label="用户名",
        validators=[DataRequired("请输入用户名")],
        description="用户名",
        render_kw={
            "id": "name",
            "class": "input-text size-L",
            "placeholder": "username"
        }
    )
    password = StringField(
        label="管理员密码",
        validators=[DataRequired("请输入密码")],
        description="密码",
        render_kw={
            "type": "password",
            "class": "input-text size-L",
            "id": "password",
            "autocomplete": "off",
            "placeholder": "密码"
        }
    )
    submit = SubmitField(render_kw={"class": "btn btn-success radius size-L", "value": "       登      录     "})
