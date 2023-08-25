from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import UserAccountCreateView, ValidateUserAccountView, RecoveryUserPassword, RecoverUserPasswordValidate, UserAccountLoginView, UserAccountLogoutView, FirstLoginChangePasswordView
router = DefaultRouter()

urlpatterns = [
    path('create-user/', UserAccountCreateView.as_view(), name='create-user'),
    path('login/', UserAccountLoginView.as_view(), name='login'),
    path('logout/', UserAccountLogoutView.as_view(), name='logout'),
    path('validate-user/', ValidateUserAccountView.as_view(), name='validate-user'),
    path('recovery-password/', RecoveryUserPassword.as_view(), name='recovery-password'),
    path('recovery-password-validate/', RecoverUserPasswordValidate.as_view(), name='recovery-password-validate'),
    path('first-login-change-password/', FirstLoginChangePasswordView.as_view(), name='first-login-change-password'),
]