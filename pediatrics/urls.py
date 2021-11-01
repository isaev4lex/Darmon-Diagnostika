from django.urls import path
from . import views

urlpatterns = [
    path('', views.pediatrics_ru, name='pediatrics_ru'),
    path('uz/', views.pediatrics_uz, name='pediatrics_uz'),
]
