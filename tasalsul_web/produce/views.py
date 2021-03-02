from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic


from .models import Product, Product_types
# Create your views here.

class IndexView(generic.ListView):
    template_name = 'produce/index.html'
    context_object_name = 'latest_product_list'

    def get_queryset(self):
        return Product.objects.all()

class DetailView(generic.DetailView):
    model = Product
    template_name = 'produce/detail.html'
    # context_object_name = 'product_types_list'

    def get_queryset(self):
        return Product.objects.all()