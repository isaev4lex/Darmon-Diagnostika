from django.urls import path
from . import views

urlpatterns = [
    path('', views.price_ru, name='price_ru'),
    path('uz/', views.price_uz, name='price_uz'),
]
