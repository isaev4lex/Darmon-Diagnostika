from django.urls import path
from . import views

urlpatterns = [
    path('', views.endocrinology_ru, name='endocrinology_ru'),
    path('uz/', views.endocrinology_uz, name='endocrinology_uz'),
    path('<slug:category_slug_ru>/', views.about_item_ru, name='endocrinology_slug_ru'),
    path('<slug:category_slug_uz>/uz/', views.about_item_uz, name='endocrinology_slug_uz'),
]
