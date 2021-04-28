from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic


from .models import Product, Product_types, Pulses, Salt, Salt_products, Meat, Meat_products, Pulses, Pulses_products
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

# Either create a new view for salt or put salt in the same index.html as above albeit with a different
# heading.

class SaltView(generic.ListView):
    template_name = 'produce/salt_index.html'
    context_object_name = 'all_salt_categories'

    def get_queryset(self):
        return Salt.objects.all()

class SaltDetailView(generic.DetailView):
    model = Salt
    template_name = 'produce/salt_detail.html'

    def get_queryset(self):
        return Salt.objects.all()

class MeatView(generic.ListView):
    template_name = 'produce/meat_index.html'
    context_object_name = 'all_meat_categories'

    def get_queryset(self):
        return Meat.objects.all()

class MeatDetailView(generic.DetailView):
    model = Meat
    template_name = 'produce/meat_detail.html'

    def get_queryset(self):
        return Meat.objects.all()

class PulsesView(generic.ListView):
    template_name = 'produce/pulses_index.html'
    context_object_name = 'all_pulses_categories'

    def get_queryset(self):
        return Pulses.objects.all()

class PulsesDetailView(generic.DetailView):
    model = Pulses
    template_name = 'produce/pulses_detail.html'

    def get_queryset(self):
        return Pulses.objects.all()