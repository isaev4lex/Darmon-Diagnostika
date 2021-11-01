from django.urls import path
from . import views

urlpatterns = [
    path('', views.routes_ru, name='routes_ru'),
    path('uz/', views.routes_uz, name='routes_uz'),
]
