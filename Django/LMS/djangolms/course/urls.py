from django.urls import path

from course import views

urlpatterns = [
    path('', views.get_courses),
    path('<slug:slug>/', views.get_course),
    path('<slug:course_slug>/<slug:lesson_slug>/', views.add_comment),
]