from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard, name="dashboard_pg"),
    
    # std based meetings urls
    
    path("meetings-class/<str:std>/", views.list_meetings, name="list_meetings_pg"),
    path("today/<str:std>/", views.today_meets, name="meetings_today"),
    path("all/<str:std>/", views.all_meets, name="meetings_all"),

    # user based meetings urls

    path("my-today-meetings", views.my_today_meets, name="mtoday_meets"),
    path("my-all-meetings", views.my_all_meets, name="mall_meets"),

    # meetings crud urls

    path("crt-meeting", views.crt_meeting, name="crt_meeting_pg"),
    path("edit-meeting/<str:pk>/", views.edit_meeting, name="edit_meeting_pg"),
    path("del-meeting/<str:id>/", views.del_meeting, name="del_meeting_pg"),
    path("restore-meeting/<str:id>/", views.rest_meeting, name="restore_meeting_pg"),
    path("conclude-meeting/<str:id>/", views.con_meeting, name="conclude_meeting_pg"),
    path("meeting-info/<str:id>/", views.meeting_info, name="meeting_info_pg"),

    # students crud url

    path("students/<str:std>/", views.all_stu, name="stu_all"),
    path('view-student/<str:rollno>/', views.view_students, name="view_student_pg"),
    path('delte-student/<str:rollno>/', views.delte_student, name="delete_student_pg"),

    # student dash operation url

    path("student-today-meets/", views.student_today_meets, name="student_today_meets_pg"),
    path("student-all-meets/", views.student_all_meets, name="student_all_meets_pg"),

    # marking attendance urls

    path("mark-attendance/<str:id>/", views.mark_attendance, name="mark_attendance_pg" )


]