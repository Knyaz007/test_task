
from rest_framework import serializers
from .models import Lesson, LessonViewed, Product

class LessonViewedSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonViewed
        fields = ['viewed_time_seconds', 'status']

class LessonSerializer(serializers.ModelSerializer):
    lessonviewed_set = LessonViewedSerializer(many=True, read_only=True)

    class Meta:
        model = Lesson
        fields = ['id', 'name', 'video_link', 'duration_seconds', 'lessonviewed_set']

class ProductStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name']

class ProductStatDetailSerializer(serializers.Serializer):
    product = ProductStatSerializer()
    total_lessons_viewed = serializers.IntegerField()
    total_time_spent = serializers.IntegerField()
    total_students = serializers.IntegerField()
    acquisition_percentage = serializers.FloatField()