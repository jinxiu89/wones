#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 18-4-1.
import os
import uuid
import datetime
from flask import jsonify, current_app, url_for


# 上传图片的前置操作
def change_filename(filename):
    fileinfo = os.path.splitext(filename)
    filename = datetime.datetime.now().strftime("%Y%m%d%H%M%S") + str(uuid.uuid4().hex) + fileinfo[-1]
    return filename


# 上传图片
def upload_image(image):
    image = image
    if not os.path.exists(current_app.config.get('IMG_DIR')):
        os.makedirs(current_app.config.get('IMG_DIR'))
        os.chmod(current_app.config.get('IMG_DIR'), 'rw')
    img = change_filename(image.filename)
    image.save(current_app.config.get('IMG_DIR') + img)
    return img


# 删除图片
def del_image(image):
    image = image
    if os.path.exists(current_app.config.get('IMG_DIR') + image):
        os.remove(current_app.config.get('IMG_DIR') + image)
    return True
