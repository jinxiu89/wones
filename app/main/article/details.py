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
    if request.method == 'GET':
        if article.count is None:
            article.count = 1
        article.count = article.count + 1
        db.session.add(article)
        db.session.commit()
    if request.method == 'POST':
        form.create()
        flash("评论成功，但是你得让我看看是不是合我的胃口^_^！", "ok")
        return redirect(request.referrer)
    return render_template('main/article/details.html', article=article, comments=comments, form=form)


@main.route("/article/details/reply", methods=['POST'])
def details_reply():
    form = ReplyForm()
    if request.method == "POST":
        if form.validate_on_submit():

            flash("评论成功，但是你得让我看看是不是合我的胃口^_^！", "ok")
            if form.create():
                flash("评论成功，但是你得让我看看是不是合我的胃口^_^！", "ok")
        else:
            flash("没保存！保存方法有问题", 'error')
        return redirect(request.referrer)
