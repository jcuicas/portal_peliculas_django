from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('next/<int:page>', views.siguiente, name='siguiente'),
    path('previous/<int:page>', views.anterior, name='anterior'),
]