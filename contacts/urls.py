from django.urls import path
from . import views

urlpatterns = [
    path('', views.contacts_ru, name='contacts_ru'),
    path('uz/', views.contacts_uz, name='contacts_uz'),
]
