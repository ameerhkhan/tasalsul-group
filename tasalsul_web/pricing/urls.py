from django.urls import path, include
from . import views
from . import price_history

urlpatterns = [
    path('', views.index, name='index'),    # has been changed to class based views so add as_view()
    path('int:products_all_id', views.detail, name='detail'),
    path('PriceHistory/', include('django_plotly_dash.urls')),
]