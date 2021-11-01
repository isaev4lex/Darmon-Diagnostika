from django.urls import path
from . import views

urlpatterns = [
    path('', views.about_us_ru, name='about_us_ru'),
    path('uz/', views.about_us_uz, name='about_us_uz'),
]
