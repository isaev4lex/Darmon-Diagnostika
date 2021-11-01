from django.shortcuts import render
from django.urls import resolve
import contacts.models as contacts
import site_settings.models as settings
from .models import *


def about_us_ru(request):
    data = {
        'meta': MetaTags.objects.all(),
        'favicons': settings.Favicon.objects.all(),
        'head_tags': settings.HeadTags.objects.all(),
        'lang': 'ru',
        'current_page_ru': resolve(request.path_info).url_name.replace(resolve(request.path_info).url_name[-2:], 'ru'),
        'current_page_uz': resolve(request.path_info).url_name.replace(resolve(request.path_info).url_name[-2:], 'uz'),
        'phones': contacts.PhoneNumbers.objects.all(),
        'emails': contacts.Emails.objects.all(),
        'addresses': contacts.Addresses.objects.all(),
    }
    contact_info = {
        'name': request.GET.get('name'),
        'surname': request.GET.get('surname'),
        'phone': request.GET.get('phone'),
    }
    if not contact_info['name'] or not contact_info['surname'] or not contact_info['phone']:
        pass
    else:
        os.system(
            f'bot_engine/main.py --name "{contact_info["name"]}" --phone "{contact_info["phone"]}" '
            f'--surname "{contact_info["surname"]}"')
        data['success_sent'] = True
    return render(request, 'about_us/index.html', context=data)


def about_us_uz(request):
    data = {
        'meta': MetaTags.objects.all(),
        'favicons': settings.Favicon.objects.all(),
        'head_tags': settings.HeadTags.objects.all(),
        'lang': 'uz',
        'current_page_ru': resolve(request.path_info).url_name.replace(resolve(request.path_info).url_name[-2:], 'ru'),
        'current_page_uz': resolve(request.path_info).url_name.replace(resolve(request.path_info).url_name[-2:], 'uz'),
        'phones': contacts.PhoneNumbers.objects.all(),
        'emails': contacts.Emails.objects.all(),
        'addresses': contacts.Addresses.objects.all(),
    }
    contact_info = {
        'name': request.GET.get('name'),
        'surname': request.GET.get('surname'),
        'phone': request.GET.get('phone'),
    }
    if not contact_info['name'] or not contact_info['surname'] or not contact_info['phone']:
        pass
    else:
        os.system(
            f'bot_engine/main.py --name "{contact_info["name"]}" --phone "{contact_info["phone"]}" '
            f'--surname "{contact_info["surname"]}"')
        data['success_sent'] = True
    return render(request, 'about_us/index.html', context=data)
