from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import MenuItem
from .urls import urlpatterns
from django.urls import path
from . import views


@receiver(post_save, sender=MenuItem)
def create_menu_item(sender, instance, created, **kwargs):
    if created:
        page_title = instance.title.lower()
        url_pattern = path(instance.url, views.menu_view, name=page_title)
        urlpatterns.append(url_pattern)
