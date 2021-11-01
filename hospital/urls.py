from django.urls import path
from . import views

urlpatterns = [
    path('', views.hospital_ru, name='hospital_ru'),
    path('uz/', views.hospital_uz, name='hospital_uz'),
]
