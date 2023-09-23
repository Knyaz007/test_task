from django.urls import path
from .views import UserLessonsListView, LessonByProductView, ProductStatDetailView

urlpatterns = [
    path('api/user_lessons/', UserLessonsListView.as_view(), name='user_lessons'),
    path('api/product_lessons/<int:pk>/', LessonByProductView.as_view(), name='product_lessons'),
    path('api/product_stats/', ProductStatDetailView.as_view(), name='product_stats'),
    # Добавьте другие URL, если у вас есть другие представления
]
