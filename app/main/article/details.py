#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 18-4-26.
from . import main
from flask import render_template, request, session, flash, redirect, url_for
from app.models.models import Article, Reply
from app.forms.reply import ReplyForm
from db_exts import db


@main.route("/article/details/<int:id>", methods=["GET", "POST"])
def article_details(id):
    article = Article.query.filter_by(id=id).first_or_404()
    comments = article.Reply.filter_by(is_show=1).order_by(Reply.id.asc())
    form = ReplyForm()
    # if int(session['count']) <= 1:
    #     if article.count is None:
    #         article.count = 1
    #     article.count = article.count + 1
    #     db.session.add(article)
    #     db.session.commit()
    if request.method == "POST":
        if form.validate_on_submit():
            data = form.data
            reply = Reply(
                content=data['content'],
                pid=data['pid'],
                article_id=data['article_id'],
                user_id=session.get("id"),
                is_show=int(2)
            )
            db.session.add(reply)
            db.session.commit()
            flash("评论成功，但是你得让我看看是不是合我的胃口^_^！", "ok")
        return redirect(url_for('main.article_details', id=article.id))
    return render_template('main/article/details.html', article=article, comments=comments, form=form)
