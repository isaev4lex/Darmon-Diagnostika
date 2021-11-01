from django.urls import path
from . import views

urlpatterns = [
    path('', views.lore_ru, name='lore_ru'),
    path('uz/', views.lore_uz, name='lore_uz'),
    path('<slug:category_slug_ru>/', views.about_item_ru, name='lore_slug_ru'),
    path('<slug:category_slug_uz>/uz/', views.about_item_uz, name='lore_slug_uz'),
]
