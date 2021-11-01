from django.urls import path
from . import views

urlpatterns = [
    path('', views.surgery_ru, name='surgery_ru'),
    path('uz/', views.surgery_uz, name='surgery_uz'),
]
