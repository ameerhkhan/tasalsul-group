from django.urls import path, include
from . import views
from .price_history import prices

app_name = 'pricing' # For the namespace error!

urlpatterns = [
    path('', views.ProductsIndexView.as_view(), name='index'),
    path('<int:pk>/', views.PlottingView.as_view(), name='detail'), # workaround for an include statement required!
    path('PriceHistory/', include('django_plotly_dash.urls')),

]

# path('<int:products_all_id>/', views.detail, include('django_plotly_dash.urls'), name='detail'),