from django.urls import path
from . import views

urlpatterns = [
    path('', views.urology_ru, name='urology_ru'),
    path('uz/', views.urology_uz, name='urology_uz'),
    path('<slug:category_slug_ru>/', views.about_item_ru, name='urology_slug_ru'),
    path('<slug:category_slug_uz>/uz/', views.about_item_uz, name='urology_slug_uz'),
]
