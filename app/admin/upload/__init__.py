#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 18-4-1.
import os
from app.admin import admin
from utils import change_filename
from flask import jsonify, request, current_app, url_for


@admin.route("/upload", methods=["POST"])
def upload():
    image = request.files['imgFile']
    if not os.path.exists(current_app.config.get('IMG_DIR')):
        os.makedirs(current_app.config.get('IMG_DIR'))
        os.chmod(current_app.config.get('IMG_DIR'), rw)
    img = change_filename(image.filename)
    image.save(current_app.config.get('IMG_DIR') + img)
    return jsonify({"error": 0, "url": url_for("static", filename="uploads/images/" + img)})
