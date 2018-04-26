#!/usr/bin/env python
# author:jinxiu89@163.com
# create by thomas on 18-1-26.
import app.models
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from create_app import app
from db_exts import db
from flask import redirect, url_for
from app.filter import *
from app.context import *


db.init_app(app)
db.app = app
db.create_all()
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command("db", MigrateCommand)

if __name__ == "__main__":
    manager.run()
