#!/usr/bin/env python
# author:jinxiu89@163.com
# create by thomas on 18-1-27.
from flask import Flask, redirect, url_for
from config import config
from .admin import admin
from .main import main


def create_app(config_name):
    app = Flask(__name__)
    # 配置加载
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    app.register_blueprint(admin)
    app.register_blueprint(main)

    @app.route("/")
    def home():
        return redirect(url_for("main.index"))

    return app
