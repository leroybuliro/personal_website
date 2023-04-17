from django.urls import path
from .controllers.signup import SubscribeView
from .controllers.signin import SigninView
from .controllers.logout import LogoutView
from .controllers.search import AuthView
from .controllers.activate import userActivationView
from .controllers.pwdreset import resetPwdView, userVerifyView
from .controllers.resMessages import AuthMsgView
from .controllers.editpassword import resetPwdEditView

app_name = "account"

urlpatterns = [
    path('auth/', AuthView, name='auth'),
    path('status/', AuthMsgView, name='authmsg'),
    path('reset/', resetPwdView, name='reset1'),
    path('reset/identifier?<uidcoded><token>/', resetPwdEditView, name='reset2'),
    path('signin/', SigninView, name='signin'),
    path('signin/verify?<uidcoded><token>/', userVerifyView, name='signinauth'),
    path('signin/activate?<uidcoded><token>/', userActivationView, name='activate'),
    path('subscribe/', SubscribeView, name='subscribe'),
    path('logout/', LogoutView, name='logout'),
]
