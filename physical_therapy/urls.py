from django.urls import path
from . import views

urlpatterns = [
    path('', views.physical_therapy_ru, name='physical_therapy_ru'),
    path('uz/', views.physical_therapy_uz, name='physical_therapy_uz'),
]
