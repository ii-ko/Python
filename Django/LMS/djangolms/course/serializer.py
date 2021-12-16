from rest_framework import serializers
from .models import Course, Lessons, Comment


class CourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'title', 'slug', 'short_description')


class CourseDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'title', 'slug', 'short_description', 'long_description')


class LessonListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lessons
        fields = ('id', 'title', 'slug', 'short_description', 'long_description')


class CommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'name', 'content', 'create_at')