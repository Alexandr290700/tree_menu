from django import template
from django.urls import reverse
from django.utils.html import format_html
from blog.models import MenuItem

register = template.Library()


@register.simple_tag
def draw_menu(menu_name):
    menu_items = MenuItem.objects.filter(menu__name=menu_name)
    return {'menu_items': menu_items}

# @register.inclusion_tag("blog/menu_detail.html", takes_context=True)
# def draw_menu(context, menu_name):
#     menu_items = MenuItem.objects.filter(name=menu_name)
#     menu_html = ""
#     for item in menu_items:
#         # создание URL
#         if item.url:
#             url = item.url
#         else:
#             url = reverse("menu_detail", args=[item.id])
#         # рекурсивный вызов для вложенных пунктов меню
#         if item.children.exists():
#             sub_menu = draw_menu(context, menu_name=item.id)
#         else:
#             sub_menu = ""
#         # форматирование HTML
#         menu_html += format_html(
#             '<li><a href="{}">{}</a>{}</li>', url, item.name, sub_menu
#         )
#     return menu_html
