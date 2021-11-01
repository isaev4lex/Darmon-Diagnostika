from django.urls import path
from . import views

urlpatterns = [
    path('', views.dermatology_ru, name='dermatology_ru'),
    path('uz/', views.dermatology_uz, name='dermatology_uz'),
    path('<slug:category_slug_ru>/', views.about_item_ru, name='dermatology_slug_ru'),
    path('<slug:category_slug_uz>/uz/', views.about_item_uz, name='dermatology_slug_uz'),
]
