# -*- coding: utf-8 -*-
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product, Lesson, LessonViewed
from .serializers import LessonSerializer, ProductStatDetailSerializer
from django.contrib.auth.models import User
from . import models
from django.db.models import Sum


class UserLessonsListView(generics.ListAPIView):
    serializer_class = LessonSerializer

    def get_queryset(self):
        user_id = self.request.user.id
        return Lesson.objects.filter(products__owner=user_id)

class LessonByProductView(generics.ListAPIView):
    serializer_class = LessonSerializer

    def get_queryset(self):
        user_id = self.request.user.id
        product_id = self.kwargs['pk']
        print(f"user_id: {user_id}, product_id: {product_id}")
        queryset = Lesson.objects.filter(products__owner=user_id, products__id=product_id)
        print(f"Queryset: {queryset}")
        return queryset

    # def get_queryset(self):
    #     user_id = self.request.user.id
    #     product_id = self.kwargs['pk']
        # return Lesson.objects.filter(products__owner=user_id, products__id=product_id)
class ProductStatDetailView(APIView):
    def get(self, request):
        products = Product.objects.all()
        stat_data = []

        for product in products:
            total_lessons_viewed = LessonViewed.objects.filter(lesson__products=product).count()
            total_time_spent = LessonViewed.objects.filter(lesson__products=product).aggregate(total_time_spent=Sum('viewed_time_seconds'))['total_time_spent']
            total_students = LessonViewed.objects.filter(lesson__products=product).values('user').distinct().count()
            total_users = User.objects.all().count()
            acquisition_percentage = (total_students / total_users) * 100

            stat_data.append({
                'product': {
                    'id': product.id,
                    'name': product.name
                },
                'total_lessons_viewed': total_lessons_viewed,
                'total_time_spent': total_time_spent,
                'total_students': total_students,
                'acquisition_percentage': acquisition_percentage
            })

        serializer = ProductStatDetailSerializer(stat_data, many=True)
        return Response(serializer.data)