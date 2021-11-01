from django.shortcuts import render
from django.urls import resolve
import contacts.models as contacts
from .models import *
import os
import site_settings.models as settings


def uzi_ru(request):
    data = {
        'meta': MetaTags.objects.all(),
        'favicons': settings.Favicon.objects.all(),
        'head_tags': settings.HeadTags.objects.all(),
        'lang': 'ru',
        'current_page_ru': 'uzi_ru',
        'current_page_uz': 'uzi_uz',
        'phones': contacts.PhoneNumbers.objects.all(),
        'emails': contacts.Emails.objects.all(),
        'addresses': contacts.Addresses.objects.all(),
        'uzi_items': UziItem.objects.all(),
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
    return render(request, 'uzi/index.html', context=data)


def uzi_uz(request):
    data = {
        'meta': MetaTags.objects.all(),
        'favicons': settings.Favicon.objects.all(),
        'head_tags': settings.HeadTags.objects.all(),
        'lang': 'uz',
        'current_page_ru': 'uzi_ru',
        'current_page_uz': 'uzi_uz',
        'phones': contacts.PhoneNumbers.objects.all(),
        'emails': contacts.Emails.objects.all(),
        'addresses': contacts.Addresses.objects.all(),
        'uzi_items': UziItem.objects.all(),
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
    return render(request, 'uzi/index.html', context=data)


def about_item_ru(request, category_slug_ru=None):
    data = {
        'meta': MetaTags.objects.all(),
        'favicons': settings.Favicon.objects.all(),
        'head_tags': settings.HeadTags.objects.all(),
        'lang': 'ru',
        'current_page_ru': 'uzi_slug_ru',
        'current_page_uz': 'uzi_slug_uz',
        'phones': contacts.PhoneNumbers.objects.all(),
        'emails': contacts.Emails.objects.all(),
        'addresses': contacts.Addresses.objects.all(),
        'uzi_items': UziItem.objects.all(),
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
    return render(request, 'about_uzi/index.html', context=data)


def about_item_uz(request, category_slug_uz=None):
    data = {
        'meta': MetaTags.objects.all(),
        'favicons': settings.Favicon.objects.all(),
        'head_tags': settings.HeadTags.objects.all(),
        'lang': 'uz',
        'current_page_ru': 'uzi_slug_ru',
        'current_page_uz': 'uzi_slug_uz',
        'phones': contacts.PhoneNumbers.objects.all(),
        'emails': contacts.Emails.objects.all(),
        'addresses': contacts.Addresses.objects.all(),
        'uzi_items': UziItem.objects.all(),
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
    return render(request, 'about_uzi/index.html', context=data)
