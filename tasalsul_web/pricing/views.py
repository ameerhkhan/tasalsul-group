from os import get_exec_path
from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, response
from pandas.core import generic
from .models import Products_all
from . import price_history

# Create your views here.

# def index(request):
#     return render(request, 'pricing/index.html')

class ProductsIndex(generic.ListView):
    template_name = 'pricing/index.html'
    context_object_name = 'products_list'

    # can also make a function here to perform the required task of generating the graph..

    def get_queryset(self):
        return Products_all.objects.all()

# def detail(request, products_all_id):
#     # response = "{} = {}".format(products_all_id, Products_all.product_price)
#     # return HttpResponse(response)
    
#     product = get_object_or_404(Products_all, pk=products_all_id)
#     # introduce logic here that will generate a pandas dataframe for that specific product.
    
#     # send that dataframe into price_history script and get back the plot.
#     # plot = price_history(dataframe_path) ?
#     return render(request, 'pricing/detail.html', {'product': product})

    # In the return statement we can also return the graph within the context manager Dictionary

    # This will help in identifying the product and now we can get its specific dataframe.