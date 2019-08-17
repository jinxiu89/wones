from functools import wraps
from flask import session, redirect, url_for, request, flash


def admin_login(f):
    """
    强制登录装饰器，检查所有的连接是否在登录状态
    :param f:
    :return:
    """

    @wraps(f)
    def req(*args, **kwargs):
        if session.get("name") is None:
            return redirect(url_for("admin.login", next=request.url))
        return f(*args, **kwargs)

    return req


def admin_permission(f):
    """
    权限检查装饰器，如果权限不够 就跳到他上一页或者首页
    :param f:
    :return:
    """

    @wraps(f)
    def req(*args, **kwargs):
        # 权限查询 如果用户名 是admin 或者 administrator 的话 拥有超级用户的权限，否则，还是去数据库查查有没有这个权限
        if session["name"] == "admin" or "administrator":
            return f(*args, **kwargs)
        else:
            from app.models.system import Permission, Role, Admin
            user = Admin.query.filter_by(name=session["name"]).first()
            role = Role.query.filter_by(id=int(user.roles)).first()
            permission = role.permissions.split(",")
            url_map = []
            query = Permission.query
            for i in permission:
                permission = query.filter_by(id=int(i)).first()
                url_map.append(permission.url)
            url = request.url_rule
            if str(url) not in url_map:
                flash("您没有权限操作", "error")
                return redirect(request.args.get("next") or url_for("admin.index"))
            return f(*args, **kwargs)

    return req


def set_count(f):
    @wraps(f)
    def req(*args, **kwargs):
        if session.get('count') is None:
            session['count'] = 1
        else:
            session['count'] = int(session.get('count')) + 1
        return f(*args, **kwargs)

    return req
