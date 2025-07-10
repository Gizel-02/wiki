from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="entry"), #step two
    path("search/", views.search, name="search"), #step 4
    path("new/", views.new_page, name="new_page"), #step 5
    path("edit/", views.edit, name="edit"), #step 6: edit page
    path("save_edit/", views.save_edit, name="save_edit"),
    path("random/", views.random, name="random") #step 7: random page
]
