from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Course
from .serializer import CourseListSerializer, CourseDetailSerializer
# Create your views here.


# mendapatkan data daftar courses
@api_view(['GET'])
def get_courses(request):
    courses = Course.objects.all()
    serializer = CourseListSerializer(courses, many=True)
    return Response(serializer.data)


# mendapatkan data detail course
@api_view(['GET'])
def get_course(request, slug):
    course = Course.objects.get(slug=slug)
    serializer = CourseDetailSerializer(course)
    return Response(serializer.data)