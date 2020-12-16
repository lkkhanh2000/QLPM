from flask_admin.contrib.sqla import ModelView
from flask_admin import expose, BaseView
from app import admin, db
from flask_login import current_user, logout_user
from app.models import NhanVien, Thuoc
from flask import redirect

class AuthenticatedView(ModelView):

    def is_accessible(self):
        return current_user.is_authenticated


class LougoutView(BaseView):
    @expose("/")
    def index(self):
        logout_user()

        return redirect("/admin")

    def is_accessible(self):
        return current_user.is_authenticated


admin.add_view(AuthenticatedView(NhanVien, db.session))
admin.add_view(AuthenticatedView(Thuoc, db.session))
admin.add_view(LougoutView(name="Logout"))