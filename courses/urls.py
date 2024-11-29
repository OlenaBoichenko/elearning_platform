from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('courses/', views.course_list, name='course_list'),
    path('<int:pk>/', views.course_detail, name='course_detail'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('create/', views.create_course, name='create_course'),
    path('manage/', views.manage_courses, name='manage_courses'),
    path('edit/<int:pk>/', views.edit_course, name='edit_course'),
    path('student_dashboard/', views.student_dashboard, name='student_dashboard'),
    path('join_course/<int:course_id>/', views.join_course, name='join_course'),
    path('available/', views.available_courses, name='available_courses'),
    path('enroll/<int:pk>/', views.enroll_course, name='enroll_course'),
    path('my_courses/', views.my_courses, name='my_courses'),
    path('course/<int:course_id>/lesson/<int:lesson_id>/', views.lesson_detail, name='lesson_detail'),
    path('complete_lesson/<int:lesson_id>/', views.complete_lesson, name='complete_lesson'),
    path('course/<int:course_id>/report/', views.course_report, name='course_report'),
    path('course/reports/', views.course_reports, name='course_reports'),
]