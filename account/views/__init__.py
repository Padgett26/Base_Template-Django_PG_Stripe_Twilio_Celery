from account.views.activate import activate
from account.views.change_pwd import change_pwd
from account.views.dashboard import dashboard
from account.views.forgotPassword import forgotPassword
from account.views.login import login
from account.views.logout import logout
from account.views.profile import profile
from account.views.register import register
from account.views.reset_password import reset_password
from account.views.resetpwd_validate import resetpwd_validate

__all__ = [
    activate,
    change_pwd,
    dashboard,
    forgotPassword,
    login,
    logout,
    profile,
    register,
    reset_password,
    resetpwd_validate,
]
