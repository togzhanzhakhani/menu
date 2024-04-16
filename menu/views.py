from django.shortcuts import render
from django.urls import path
from django.http import Http404
from .models import MenuItem

def menu_view(request, menu_url):
    try:
        menu_items = MenuItem.objects.filter(url=menu_url)
        print(menu_url)
    except MenuItem.DoesNotExist:
        raise Http404("Страница не найдена")
    return render(request, 'menu.html', {'menu_items': menu_items})


def home(request):
    menu_items = MenuItem.objects.filter(parent__isnull=True)
    return render(request, 'home.html', {'menu_items': menu_items})


def generate_urls():
    urls = []
    menus = MenuItem.objects.all()
    for menu in menus:
        page_title = menu.title.lower()
        urls.append(path(f'{page_title}/', menu_view, name=f'{page_title}'))
    return urls

