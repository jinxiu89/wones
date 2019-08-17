#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 18-7-26.
from app.forms import *
from app.models.models import Reply
from db_exts import db
from flask import session


class ReplyForm(FlaskForm):
    content = TextAreaField(label="评论内容",
                            description="评论内容",
                            validators=[DataRequired("没有评论咋存呢？占空地？")],
                            render_kw={"id": "content",
                                       "class": "form-control",
                                       "placeholder": "评论内容",
                                       "rows": "10"
                                       })
    pid = IntegerField()
    article_id = IntegerField()
    user_id = IntegerField()
    submit = SubmitField(
        render_kw={"class": "btn btn-success radius size-L", "value": "       保      存     "})

    def create(self):
        reply = Reply(
            content=self.content.data,
            # pid=self.pid.data,
            article_id=self.article_id.data,
            # user_id=session.get("id"),
            is_show=int(2)
        )
        db.session.add(reply)
        db.session.commit()
        return reply
