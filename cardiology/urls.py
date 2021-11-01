from django.urls import path
from . import views

urlpatterns = [
    path('', views.cardiology_ru, name='cardiology_ru'),
    path('uz/', views.cardiology_uz, name='cardiology_uz'),
    path('<slug:category_slug_ru>/', views.about_item_ru, name='cardiology_slug_ru'),
    path('<slug:category_slug_uz>/uz/', views.about_item_uz, name='cardiology_slug_uz'),
]
