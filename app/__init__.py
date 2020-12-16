from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_login import LoginManager

app = Flask(__name__)
app.secret_key = "C1\r\x99\x9f?\xb4\x06B)KJ\x12\xea\xd8,"
app.config["SQLALCHEMY_DATABASE_URI"] ="mysql+pymysql://root:12345sau@localhost/qlphongmach?charset=utf8mb4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app=app)


admin = Admin(app=app, name="DANH SACH BENH NHAN", template_mode="bootstrap3")


login = LoginManager(app=app)