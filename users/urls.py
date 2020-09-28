from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.user_login, name="login_pg"),
    path('register/', views.student_register, name="registration_pg"),
    path('register-te@cher-qwyin/', views.teacher_register, name="teacher_registeration_pg"),
    path('logout/', views.user_logout, name="logout_pg"),

    # password management urls

    path('reset_password/', auth_views.PasswordResetView.as_view(), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]