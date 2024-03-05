from django.urls import path

from account import views

app_name = "account"
urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("activate/", views.activate, name="activate"),
    path("forgotPassword/", views.forgotPassword, name="forgotPassword"),
    path("reset_password/", views.reset_password, name="reset_password"),
    path(
        "resetpwd_validate/",
        views.resetpwd_validate,
        name="resetpwd_validate",
    ),
    path("profile/", views.profile, name="profile"),
    path("change_pwd/", views.change_pwd, name="change_pwd"),
]
