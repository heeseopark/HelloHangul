from django.urls import include, path

from . import views

app_name = 'ktalk'

urlpatterns = [
    path('theme/', views.theme, name='theme'),
    path('add_theme/', views.add_theme, name='add_theme'),
    path('delete_theme/<int:theme_id>/', views.delete_theme, name='delete_theme'),
    path('init/', views.index, name='index'),
    path('init/<int:theme_id>/', views.index, name='index_with_theme'),
    
]