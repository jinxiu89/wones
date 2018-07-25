#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 18-4-28.
from app.forms import *
from app.models.models import Friends
from db_exts import db
from utils import upload_image, del_image
from datetime import datetime


class FriendForm(FlaskForm):
    name = StringField(label="网站名称",
                       description="网站名称",
                       render_kw={"id": "name",
                                  "class": "input-text size-L",
                                  "placeholder": "网站名称"
                                  })
    website_logo = FileField(label="图片地址",
                             description='图片地址',
                             render_kw={"class": "btn btn-default",
                                        "style": "height:37px"})
    website = StringField(label="指向路径",
                          description="指向路径",
                          render_kw={"id": "path",
                                     "class": "input-text size-L",
                                     "placeholder": "http://"})
    is_show = SelectField(label="状态",
                          validators={DataRequired("必须选择一个")},
                          coerce=int,
                          choices=[(1, '启用'), (2, '禁用')],
                          render_kw={"class": "select valid",
                                     "size": 1, "style": "height:30px"})
    submit = SubmitField(render_kw={"class": "btn btn-success radius size-L", "value": "       保      存     "})

    def create(self):
        friend = Friends(
            name=self.name.data,
            website_logo=upload_image(self.website_logo.data),
            website=self.website.data,
            is_show=self.is_show.data
        )
        db.session.add(friend)
        db.session.commit()
        return friend

    def edit(self, friend):
        friend.name = self.name.data
        if self.website_logo.data:
            if friend.website_logo is not None:
                del_image(friend.website_logo)
            friend.website_logo = upload_image(self.website_logo.data)
        friend.website = self.website.data
        friend.is_show = self.is_show.data
        db.session.add(friend)
        db.session.commit()
        return friend
