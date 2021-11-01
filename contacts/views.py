from django.shortcuts import render
from django.urls import resolve
from .models import *
import site_settings.models as settings


def contacts_ru(request):
    data = {
        'meta': MetaTags.objects.all(),
        'favicons': settings.Favicon.objects.all(),
        'head_tags': settings.HeadTags.objects.all(),
        'lang': 'ru',
        'current_page_ru': resolve(request.path_info).url_name.replace(resolve(request.path_info).url_name[-2:], 'ru'),
        'current_page_uz': resolve(request.path_info).url_name.replace(resolve(request.path_info).url_name[-2:], 'uz'),
        'phones': PhoneNumbers.objects.all(),
        'emails': Emails.objects.all(),
        'addresses': Addresses.objects.all(),
    }
    return render(request, 'contacts/index.html', context=data)


def contacts_uz(request):
    data = {
        'meta': MetaTags.objects.all(),
        'favicons': settings.Favicon.objects.all(),
        'head_tags': settings.HeadTags.objects.all(),
        'lang': 'uz',
        'current_page_ru': resolve(request.path_info).url_name.replace(resolve(request.path_info).url_name[-2:], 'ru'),
        'current_page_uz': resolve(request.path_info).url_name.replace(resolve(request.path_info).url_name[-2:], 'uz'),
        'phones': PhoneNumbers.objects.all(),
        'emails': Emails.objects.all(),
        'addresses': Addresses.objects.all(),
    }
    return render(request, 'contacts/index.html', context=data)
