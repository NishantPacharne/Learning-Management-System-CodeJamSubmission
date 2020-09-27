from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_login, name="login_pg"),
    path('register/', views.student_register, name="registration_pg"),
    path('register-te@cher-qwyin/', views.teacher_register, name="teacher_registeration_pg"),
    path('logout/', views.user_logout, name="logout_pg")
]