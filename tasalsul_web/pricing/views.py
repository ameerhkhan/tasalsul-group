from os import get_exec_path
from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, response

from django.views import generic
# from numpy.core.fromnumeric import product
from .models import Products_all
import pandas as pd



from django.utils import timezone
from datetime import datetime

from .price_history import prices

# from django_plotly_dash import DjangoDash

# Create your views here.


class ProductsIndexView(generic.ListView):
    template_name = 'pricing/index.html'
    context_object_name = 'products_list'
    paginate_by = 15

    def get_queryset(self):
        # return Products_all.objects.all()
        return Products_all.objects.filter(price_date__lte=timezone.now()).order_by('-price_date')[:]


class PlottingView(generic.DetailView):       # use detail view instead of templateview
    model = Products_all
    template_name = 'pricing/detail.html'

    def get_queryset(self):
        self.product = get_object_or_404(Products_all, pk=self.kwargs['pk'])
        name = self.product.product_name
        return Products_all.objects.filter(product_name = name)
        
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        product = self.product
        product_name = product.product_name
        
        fig = prices(product_name)
        graph = fig.to_html(full_html=False, default_height=600, default_width=600)
        # graph = fig.to_html(full_html=False)
        
        context['product'] = product
        context['graph'] = graph

        return context