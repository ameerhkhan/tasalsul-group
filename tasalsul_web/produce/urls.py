from django.urls import path

from . import views

app_name = 'produce'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('salt', views.SaltView.as_view(), name='salt_index'),
    path('salt/<int:pk>/', views.SaltDetailView.as_view(), name='salt_detail'),
    path('meat', views.MeatView.as_view(), name='meat_index'),
    path('meat/<int:pk>/', views.MeatDetailView.as_view(), name='meat_detail'),
    path('pulses', views.PulsesView.as_view(), name='pulses_index'),
    path('pulses/<int:pk>/', views.PulsesDetailView.as_view(), name='pulses_detail'),
]