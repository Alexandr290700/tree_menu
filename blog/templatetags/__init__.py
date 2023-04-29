from django import template
from ..models import MenuItem

register = template.Library()

@register.simple_tag
def draw_menu():
    return MenuItem.objects.first()

