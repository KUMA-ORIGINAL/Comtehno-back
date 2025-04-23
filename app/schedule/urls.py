from django.urls import path
from . import views

urlpatterns = [
    path('groups/course/<int:course_year>/', views.GroupListByCourseView.as_view(), name='group-list-by-course'),
    path('schedule/group/<int:group_id>/<str:weekday>/', views.ScheduleByGroupView.as_view(), name='group-schedule'),
    path('schedule/group/<int:group_id>/<str:weekday>/<str:week_type>/', views.ScheduleByGroupView.as_view(), name='group-schedule-weektype'),
    
    path('teachers/', views.TeacherListView.as_view(), name='teacher-list'),
    path('schedule/teacher/<int:teacher_id>/<str:weekday>/', views.ScheduleByTeacherView.as_view(), name='teacher-schedule'),
    path('schedule/teacher/<int:teacher_id>/<str:weekday>/<str:week_type>/', views.ScheduleByTeacherView.as_view(), name='teacher-schedule-weektype'),
]
