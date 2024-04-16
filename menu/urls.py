from django.urls import path
from .models import MenuItem
from . import views


urlpatterns = [
    path('menu/<str:menu_url>/', views.menu_view, name='menu_view'),
    path('', views.home, name='home'),
]

def generate_urls():
    urls = []
    menus = MenuItem.objects.all()
    for menu in menus:
        page_title = menu.title.lower()
        urls.append(path(f'{menu.url}/', views.menu_view, name=f'{page_title}'))
    return urls

urlpatterns += generate_urls()
