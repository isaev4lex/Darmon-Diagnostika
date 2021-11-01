from django.urls import path
from . import views

urlpatterns = [
    path('', views.therapist_ru, name='therapist_ru'),
    path('uz/', views.therapist_uz, name='therapist_uz'),
    path('<slug:category_slug_ru>/', views.about_item_ru, name='therapist_slug_ru'),
    path('<slug:category_slug_uz>/uz/', views.about_item_uz, name='therapist_slug_uz'),
]
