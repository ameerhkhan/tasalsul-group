from os import get_exec_path
from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, response

from django.views import generic
from numpy.core.fromnumeric import product
from .models import Products_all
from .price_history import prices
import pandas as pd

import dash
import dash_core_components as dcc
import dash_html_components as html

import plotly.express as px
from django.utils import timezone
from datetime import datetime

# from django_plotly_dash import DjangoDash

# Create your views here.


class ProductsIndexView(generic.ListView):
    template_name = 'pricing/index.html'
    context_object_name = 'products_list'
    paginate_by = 15

    def get_queryset(self):
        return Products_all.objects.all()

# def detail(request, products_all_id):   # turn into class based view??    
#     product = get_object_or_404(Products_all, pk=products_all_id)
#     product_name = product.product_name
#     df = pd.read_csv('pricing/assets/historical_pricing.csv')
#     df_copy = df.copy()

#     product_df = df_copy.loc[df['NAME'] == product_name]

#     x = product_df['DATE'].to_list()
#     y = product_df['PRICE'].to_list()
    
#     current_year = datetime.today().year

#     fig = px.line(df, x, y)

#     colors = {
#     'background': 'black',
#     'paper': 'black',
#     'text': 'navajowhite'
#     }

#     fig.update_layout(
#     plot_bgcolor=colors['background'], # background
#     paper_bgcolor=colors['paper'],     # graph area
#     font_color=colors['text']          # text
#     )



#     print(product_df)
#     # plot = prices(product_df)

#     graph = fig.to_html(full_html=False, default_height=500, default_width=700)

#     context_dic = {
#         'product': product,
#         'graph': graph
#     }
#     return render(request, 'pricing/detail.html', context=context_dic)



# from https://stackoverflow.com/questions/36846395/embedding-a-plotly-chart-in-a-django-template

# https://docs.djangoproject.com/en/3.2/ref/class-based-views/generic-display/#detailview

class PlottingView(generic.DetailView):       # use detail view instead of templateview
    model = Products_all
    template_name = 'pricing/detail.html'

    def get_queryset(self):
        # self.product = get_object_or_404(Products_all, pk=self.kwargs['products_all_id'])
        self.product = get_object_or_404(Products_all, pk=self.kwargs['pk'])
        name = self.product.product_name
        return Products_all.objects.filter(product_name = name)
        # product_name = product.product_name
        # df = pd.read_csv('pricing/assets/historical_pricing.csv')
        # df_copy = df.copy()

        # product_df = df_copy.loc[df['NAME'] == product_name]
        # x = product_df['DATE'].to_list()
        # y = product_df['PRICE'].to_list()



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # product = get_object_or_404(Products_all, pk=self.kwargs['products_all_id'])
        product = self.product
        product_name = product.product_name
        df = pd.read_csv('pricing/assets/historical_pricing.csv')
        df_copy = df.copy()

        product_df = df_copy.loc[df['NAME'] == product_name]
        x = product_df['DATE'].to_list()
        y = product_df['PRICE'].to_list()

        fig = px.line(df, x, y)
        colors = {
        'background': 'black',
        'paper': 'black',
        'text': 'navajowhite'
        }
        fig.update_layout(
        plot_bgcolor=colors['background'], # background
        paper_bgcolor=colors['paper'],     # graph area
        font_color=colors['text']          # text
        )

        graph = fig.to_html(full_html=False, default_height=500, default_width=700)
        context['product'] = product
        context['graph'] = graph

        return context

    #   context['now'] = timezone.now()
    #   return context    



