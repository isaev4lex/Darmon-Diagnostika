from django.urls import path
from . import views

urlpatterns = [
    path('', views.operating_unit_ru, name='operating_unit_ru'),
    path('uz/', views.operating_unit_uz, name='operating_unit_uz'),
]
