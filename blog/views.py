from django.shortcuts import render, get_object_or_404
from .models import MenuItem


# def home(request, pk=None):
#     context = {}
#     return render(request, 'blog/index.html', context)


def menu_list(request):
    menu_items = MenuItem.objects.all()
    return render(request, "index.html", {"menu_items": menu_items})


def menu_detail(request, item_id):
    item = get_object_or_404(MenuItem, id=item_id)
    return render(request, "blog/menu_detail.html", {"item": item})
