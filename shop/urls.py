from django.urls import path
from .import views


urlpatterns = [
    path("", views.index),
    path("search", views.search),
    path("products/<int:myid>", views.productView),
    path("checkout", views.checkout)


]