from django.urls import path
from . import views

urlpatterns = [
    path('', views.neuropathologist_ru, name='neuropathologist_ru'),
    path('uz/', views.neuropathologist_uz, name='neuropathologist_uz'),
    path('<slug:category_slug_ru>/', views.about_item_ru, name='neuropathologist_slug_ru'),
    path('<slug:category_slug_uz>/uz/', views.about_item_uz, name='neuropathologist_slug_uz'),
]
