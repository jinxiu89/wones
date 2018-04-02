#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 18-1-27.
from . import main


@main.route("/")
def index():
    return "main hello!"


@main.route("/login", methods=["GET", "POST"])
def login():
    return "login"
