from django.urls import path
from . import views

urlpatterns = [
    path('', views.neuropathologist_kids_ru, name='neuropathologist_kids_ru'),
    path('uz/', views.neuropathologist_kids_uz, name='neuropathologist_kids_uz'),
]
