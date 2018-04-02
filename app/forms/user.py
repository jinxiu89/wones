#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 18-3-18.
from app.forms import *


class UserForm(FlaskForm):
    name = StringField(
        label="管理员名",
        validators=[DataRequired("请输入管理员名")],
        description="管理员名",
        render_kw={
            "class": "input-text",
            "placeholder": "请输入管理员名，例如：admin",
            "id": "name",
        }
    )
    password = StringField(
        label="管理员密码",
        validators=[DataRequired("请输入密码")],
        description="密码",
        render_kw={
            "type": "password",
            "class": "input-text",
            "id": "password",
            "autocomplete": "off",
            "placeholder": "密码"
        }
    )
    is_admin = SelectField(
        label="是否是管理员",
        validators={
            DataRequired("必须选择一个")
        },
        coerce=int,
        choices=[(1, '是'), (2, '否')],
        render_kw={
            "class": "select valid",
            "size": 1
        }

    )

    description = TextAreaField(
        label="备注",
        description="备注",
        render_kw={
            "class": "textarea",
            "cols": "",
            "rows": "",
            "placeholder": "100字以内随便打",
            "dragonfly": "true",
        }
    )
    submit = SubmitField(render_kw={"class": "btn btn-primary radius", "value": "保存提交"})