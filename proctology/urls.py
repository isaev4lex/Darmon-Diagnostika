from django.urls import path
from . import views

urlpatterns = [
    path('', views.proctology_ru, name='proctology_ru'),
    path('uz/', views.proctology_uz, name='proctology_uz'),
    path('<slug:category_slug_ru>/', views.about_item_ru, name='proctology_slug_ru'),
    path('<slug:category_slug_uz>/uz/', views.about_item_uz, name='proctology_slug_uz'),
]
