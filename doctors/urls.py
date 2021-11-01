from django.urls import path
from . import views

urlpatterns = [
    path('', views.doctors_ru, name='doctors_ru'),
    path('uz/', views.doctors_uz, name='doctors_uz'),
    path('<slug:doctor_slug_ru>/', views.about_doctor_ru, name='doctor_slug_ru'),
    path('<slug:doctor_slug_uz>/uz/', views.about_doctor_uz, name='doctor_slug_uz'),
]
