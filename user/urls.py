from django.contrib.auth import views
from django.contrib.auth import views
from django.urls import path

from .views import *


urlpatterns = [
    path('policy/',policy,name="policy"),

    path('register/',register,name="register"),
    path('login/',views.LoginView.as_view(template_name='login.html'),name="login"),
    path('logout/',views.LogoutView.as_view(template_name='logout.html'),name="logout"),
    path('profile/<str:id>/',profile,name="profile"),
    path('profile/<str:id>/edit/',profile_edit,name="profile_edit"),
    path('password_change/',views.PasswordChangeView.as_view(template_name="password_change_form.html"),name="password_change"),
    path('password_change_done/',views.PasswordChangeDoneView.as_view(template_name="password_change_done.html"),name="password_change_done"),

    path('password-reset/',views.PasswordResetView.as_view(template_name='reset/password_reset_form.html'),name="password_reset"),
    path('password-reset/done/',views.PasswordResetDoneView.as_view(template_name='reset/password_reset_done.html'),name="password_reset_done"),
    path('password-reset-confirm/<uidb64>/<token>/',views.PasswordResetConfirmView.as_view(template_name='reset/password_reset_confirm.html'),name="password_reset_confirm"),
    path('password-reset-complete',views.PasswordResetCompleteView.as_view(template_name='reset/password_reset_complete.html'),name="password_reset_complete"),

]