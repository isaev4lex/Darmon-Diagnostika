from django.urls import path
from . import views

urlpatterns = [
    path('', views.stomatology_ru, name='stomatology_ru'),
    path('uz/', views.stomatology_uz, name='stomatology_uz'),
]
