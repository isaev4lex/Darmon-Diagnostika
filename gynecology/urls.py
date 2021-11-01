from django.urls import path
from . import views

urlpatterns = [
    path('', views.gynecology_ru, name='gynecology_ru'),
    path('uz/', views.gynecology_uz, name='gynecology_uz'),
    path('<slug:category_slug_ru>/', views.about_item_ru, name='gynecology_slug_ru'),
    path('<slug:category_slug_uz>/uz/', views.about_item_uz, name='gynecology_slug_uz'),
]
