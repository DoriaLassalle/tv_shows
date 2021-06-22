from django.urls import path
from . import views

urlpatterns=[
    path('', views.empty),
    path('shows', views.index),    
    path('shows/new', views.addShowTemp),
    path('shows/add', views.addShow),
    path('shows/<id>', views.showCreated),
    path('shows/create/<id>', views.showCreated),
    path('shows/<id>/edit', views.editShow),
    path('shows/<id>/update', views.update),
    path('shows/<id>/destroy', views.destroy)
]