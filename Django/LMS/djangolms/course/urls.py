from django.urls import path

from course import views

urlpatterns = [
    path('', views.get_courses),
    path('get_frontpage_courses/', views.get_frontpage_courses),
    path('<slug:slug>/', views.get_course),
    path('<slug:course_slug>/<slug:lesson_slug>/', views.add_comment),
    path('<slug:course_slug>/<slug:lesson_slug>/comments/', views.get_comments),
]