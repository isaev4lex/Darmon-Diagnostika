from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_ru, name='home_ru'),
    path('uz/', views.home_uz, name='home_uz'),
]
