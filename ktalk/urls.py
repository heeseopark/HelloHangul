from django.urls import include, path

from . import views

urlpatterns = [
    path('init/', views.index),
]