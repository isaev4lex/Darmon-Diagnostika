from django.shortcuts import render
from django.urls import resolve
import contacts.models as contacts
from .models import *
import os
import site_settings.models as settings


def pediatrics_ru(request):
    data = {
        'meta': MetaTags.objects.all(),
        'favicons': settings.Favicon.objects.all(),
        'head_tags': settings.HeadTags.objects.all(),
        'lang': 'ru',
        'current_page_ru': 'pediatrics_ru',
        'current_page_uz': 'pediatrics_uz',
        'phones': contacts.PhoneNumbers.objects.all(),
        'emails': contacts.Emails.objects.all(),
        'addresses': contacts.Addresses.objects.all(),
        'pediatrics_items': PediatricsItem.objects.all(),
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
    return render(request, 'pediatrics/index.html', context=data)


def pediatrics_uz(request):
    data = {
        'meta': MetaTags.objects.all(),
        'favicons': settings.Favicon.objects.all(),
        'head_tags': settings.HeadTags.objects.all(),
        'lang': 'uz',
        'current_page_ru': 'pediatrics_ru',
        'current_page_uz': 'pediatrics_uz',
        'phones': contacts.PhoneNumbers.objects.all(),
        'emails': contacts.Emails.objects.all(),
        'addresses': contacts.Addresses.objects.all(),
        'pediatrics_items': PediatricsItem.objects.all(),
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
    return render(request, 'pediatrics/index.html', context=data)