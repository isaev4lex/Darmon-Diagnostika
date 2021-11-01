from django.shortcuts import render
from django.urls import resolve
import contacts.models as contacts
from .models import *
from random import choice
import os
import site_settings.models as settings


def doctors_ru(request):
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
        'doctors': Doctors.objects.all(),
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
    return render(request, 'doctors/index.html', context=data)


def doctors_uz(request):
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
        'doctors': Doctors.objects.all(),
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
    return render(request, 'doctors/index.html', context=data)


def about_doctor_ru(request, doctor_slug_ru=None):
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
        'doctors': Doctors.objects.all(),
        'random_doctors': [],
        'no_lang_menu': True,
        'slug': doctor_slug_ru
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
    if len(Doctors.objects.all()) > 3:
        while len(data['random_doctors']) != 3:
            random = choice(Doctors.objects.all())
            if random not in data['random_doctors']:
                data['random_doctors'].append(random)
    return render(request, 'about_doctor/index.html', context=data)


def about_doctor_uz(request, doctor_slug_uz=None):
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
        'doctors': Doctors.objects.all(),
        'random_doctors': [],
        'no_lang_menu': True,
        'slug': doctor_slug_uz
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
    if len(Doctors.objects.all()) > 3:
        while len(data['random_doctors']) != 3:
            random = choice(Doctors.objects.all())
            if random not in data['random_doctors']:
                data['random_doctors'].append(random)
    return render(request, 'about_doctor/index.html', context=data)
