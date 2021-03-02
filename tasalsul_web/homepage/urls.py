from django.urls import path

from . import views

app_name = 'homepage'

urlpatterns = [
    path('', views.index, name='index'),
    path('message_sent/', views.message_sent, name='message_sent'),
]