from django.urls import path
from . import views

urlpatterns = [
    path('', views.xray_ru, name='xray_ru'),
    path('uz/', views.xray_uz, name='xray_uz'),
]
