from django.shortcuts import render
from django.urls import resolve
import contacts.models as contacts
from .models import *
import os
import site_settings.models as settings


def neuropathologist_ru(request):
    data = {
        'meta': MetaTags.objects.all(),
        'favicons': settings.Favicon.objects.all(),
        'head_tags': settings.HeadTags.objects.all(),
        'lang': 'ru',
        'current_page_ru': 'neuropathologist_ru',
        'current_page_uz': 'neuropathologist_uz',
        'phones': contacts.PhoneNumbers.objects.all(),
        'emails': contacts.Emails.objects.all(),
        'addresses': contacts.Addresses.objects.all(),
        'neuropathologist_items': NeuropathologistItem.objects.all(),
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
    return render(request, 'neuropathologist/index.html', context=data)


def neuropathologist_uz(request):
    data = {
        'meta': MetaTags.objects.all(),
        'favicons': settings.Favicon.objects.all(),
        'head_tags': settings.HeadTags.objects.all(),
        'lang': 'uz',
        'current_page_ru': 'neuropathologist_ru',
        'current_page_uz': 'neuropathologist_uz',
        'phones': contacts.PhoneNumbers.objects.all(),
        'emails': contacts.Emails.objects.all(),
        'addresses': contacts.Addresses.objects.all(),
        'neuropathologist_items': NeuropathologistItem.objects.all(),
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
    return render(request, 'neuropathologist/index.html', context=data)


def about_item_ru(request, category_slug_ru=None):
    data = {
        'meta': MetaTags.objects.all(),
        'favicons': settings.Favicon.objects.all(),
        'head_tags': settings.HeadTags.objects.all(),
        'lang': 'ru',
        'current_page_ru': 'neuropathologist_slug_ru',
        'current_page_uz': 'neuropathologist_slug_uz',
        'phones': contacts.PhoneNumbers.objects.all(),
        'emails': contacts.Emails.objects.all(),
        'addresses': contacts.Addresses.objects.all(),
        'neuropathologist_items': NeuropathologistItem.objects.all(),
        'slug': category_slug_ru
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
    return render(request, 'about_neuropathologist/index.html', context=data)


def about_item_uz(request, category_slug_uz=None):
    data = {
        'meta': MetaTags.objects.all(),
        'favicons': settings.Favicon.objects.all(),
        'head_tags': settings.HeadTags.objects.all(),
        'lang': 'uz',
        'current_page_ru': 'neuropathologist_slug_ru',
        'current_page_uz': 'neuropathologist_slug_uz',
        'phones': contacts.PhoneNumbers.objects.all(),
        'emails': contacts.Emails.objects.all(),
        'addresses': contacts.Addresses.objects.all(),
        'neuropathologist_items': NeuropathologistItem.objects.all(),
        'slug': category_slug_uz
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
    return render(request, 'about_neuropathologist/index.html', context=data)
