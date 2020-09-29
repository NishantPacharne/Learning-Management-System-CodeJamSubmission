from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.user_login, name="login_pg"),
    path('register/', views.student_register, name="registration_pg"),
    path('register-te@cher-qwyin/', views.teacher_register, name="teacher_registeration_pg"),
    path('logout/', views.user_logout, name="logout_pg"),

    # password management urls

    path('reset-password/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='reset_password'),
    path('reset-password/sent/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset-password/complete/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),

]