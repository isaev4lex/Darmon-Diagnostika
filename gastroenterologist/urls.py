from django.urls import path
from . import views

urlpatterns = [
    path('', views.gastroenterologist_ru, name='gastroenterologist_ru'),
    path('uz/', views.gastroenterologist_uz, name='gastroenterologist_uz'),
    path('<slug:category_slug_ru>/', views.about_item_ru, name='gastroenterologist_slug_ru'),
    path('<slug:category_slug_uz>/uz/', views.about_item_uz, name='gastroenterologist_slug_uz'),
]
