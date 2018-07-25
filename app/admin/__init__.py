#!/usr/bin/env python
# author:jinxiu89@163.com
# create by thomas on 18-1-27.
from flask import Blueprint

admin = Blueprint("admin", __name__, url_prefix="/admin")
from .system import user, category
from .content import article, banner, ad, friend
from .dashboard import index
from .login import login, logout
from .upload import upload
