from django.urls import path
from . import views

urlpatterns = [
    path('', views.laboratory_ru, name='laboratory_ru'),
    path('uz/', views.laboratory_uz, name='laboratory_uz'),
    path('<slug:category_slug_ru>/', views.about_item_ru, name='lab_slug_ru'),
    path('<slug:category_slug_uz>/uz/', views.about_item_uz, name='lab_slug_uz'),
]
