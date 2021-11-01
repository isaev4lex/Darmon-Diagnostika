from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', include('main_page.urls')),
    
    
    path('robots.txt', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
    path('sitemap.xml', TemplateView.as_view(template_name='sitemap.xml', content_type='text/xml')),
    
    path('routes/', include('routes.urls')),
    path('laboratory/', include('laboratory.urls')),
    path('uzi/', include('uzi.urls')),
    path('xray/', include('xray.urls')),
    path('gynecology/', include('gynecology.urls')),
    path('cardiology/', include('cardiology.urls')),
    path('urology/', include('urology.urls')),
    path('endocrinology/', include('endocrinology.urls')),
    path('proctology/', include('proctology.urls')),
    path('dermatology/', include('dermatology.urls')),
    path('stomatology/', include('stomatology.urls')),
    path('lore/', include('lore.urls')),
    path('pediatrics/', include('pediatrics.urls')),
    path('neuropathologist/', include('neuropathologist.urls')),
    path('therapist/', include('therapist.urls')),
    path('surgery/', include('surgery.urls')),
    path('hospital/', include('hospital.urls')),
    path('gastroenterologist/', include('gastroenterologist.urls')),
    path('physical_therapy/', include('physical_therapy.urls')),
    path('neuropathologist_kids/', include('neuropathologist_kids.urls')),
    path('operating_unit/', include('operating_unit.urls')),
    path('about_us/', include('about_us.urls')),
    path('contacts/', include('contacts.urls')),
    path('price/', include('price.urls')),
    path('doctors/', include('doctors.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
