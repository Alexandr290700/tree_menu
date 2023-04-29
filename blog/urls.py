from django.urls import path
from .views import menu_detail, menu_list

urlpatterns = [
    path("", menu_list, name="menu_list"),
    path("menu/<int:item_id>/", menu_detail, name="menu_detail"),
]
