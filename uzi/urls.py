from django.urls import path
from . import views

urlpatterns = [
    path('', views.uzi_ru, name='uzi_ru'),
    path('uz/', views.uzi_uz, name='uzi_uz'),
    path('<slug:category_slug_ru>/', views.about_item_ru, name='uzi_slug_ru'),
    path('<slug:category_slug_uz>/uz/', views.about_item_uz, name='uzi_slug_uz'),
]
