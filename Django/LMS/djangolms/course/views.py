from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Course, Lessons, Comment
from .serializer import CourseListSerializer, CourseDetailSerializer, \
    LessonListSerializer, CommentListSerializer
# Create your views here.


# mendapatkan data daftar courses
@api_view(['GET'])
def get_courses(request):
    courses = Course.objects.all()
    serializer = CourseListSerializer(courses, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_frontpage_courses(request):
    courses = Course.objects.all()[0:4]
    serializer = CourseListSerializer(courses, many=True)
    return Response(serializer.data)


# mendapatkan data detail course dan lesson
@api_view(['GET'])
def get_course(request, slug):
    course = Course.objects.get(slug=slug)
    course_serializer = CourseDetailSerializer(course)
    lesson_serializer = LessonListSerializer(course.lessons.all(), many=True)

    data = {
        'course': course_serializer.data,
        'lesson': lesson_serializer.data
    }

    return Response(data)


@api_view(['GET'])
def get_comments(request, course_slug, lesson_slug):
    lesson = Lessons.objects.get(slug=lesson_slug)
    serializer = CommentListSerializer(lesson.comments.all(), many=True)
    return Response(serializer.data)


@api_view(['POST'])
def add_comment(request, course_slug, lesson_slug):
    data = request.data
    name = data.get('name')
    content = data.get('content')

    course = Course.objects.get(slug=course_slug)
    lesson = Lessons.objects.get(slug=lesson_slug)

    comment = Comment.objects.create(course=course, lesson=lesson, name=name,
                                     content=content, create_by=request.user)

    serializer = CommentListSerializer(comment)
    return Response(serializer.data)