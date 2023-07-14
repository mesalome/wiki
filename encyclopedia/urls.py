from django.urls import path

from . import views

app_name = "encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("<str:title>", views.entry_page, name="title"),
    path("search/", views.search, name = "search"),
    path("createpage/", views.create_page, name = "newpage"),
    path("addpage/", views.add_page, name="add"),
    path("edit/", views.edit, name = "edit"),
    path("save/", views.save, name="save" ),
    path("random/", views.random, name="random"),
]
