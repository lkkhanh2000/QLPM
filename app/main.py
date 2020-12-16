from flask import render_template, redirect, request, url_for, session
from app import app, login, utils
from flask_login import login_user, login_required
from app.models import *
from app.admin import *


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/BN")
def BN_list():
    maBN = request.args.get("maBN")
    kw = request.args.get("kw")
    benhnhan = utils.read_benhnhan(maBN=maBN, kw=kw)

    return render_template("BN-list.html", benhnhan=benhnhan)


@app.route("/login-user", methods=["get", "post"])
def login_users():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password", "")
        user = utils.check_login_user(username=username,
                                      password=password)
        if user:
            login_user(user=user)

    return redirect("/")


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))


@app.route('/register', methods=['get', 'post'])
def register():
    err_msg = ""
    if request.method == 'POST':
        password = request.form.get('password')
        confirm = request.form.get('confirm')
        if password == confirm:
            name = request.form.get('name')
            username = request.form.get('username')
            if utils.add_user(name=name, username=username,
                              password=password):
                return redirect('/login')
            else:
                err_msg = "Hệ thống đang có lỗi! Vui lòng quay lại sau!"
        else:
            err_msg = "Mật khẩu KHÔNG khớp!"

    return render_template('register.html', err_msg=err_msg)


@app.route("/login-admin", methods=["post"])
def login_admin():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password", "")
        user = utils.check_login(username=username,
                                 password=password)
        if user:
            login_user(user=user)

    return redirect("/admin")


@login.user_loader
def get_user(user_id):
    return utils.get_user_by_id(user_id=user_id)


@app.route("/index/add-ds")
def add_or_update_ds():
    return render_template("add-ds.html")


if __name__ == "__main__":
    app.run(debug=True)
