from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .forms import ProductForm
from django.views.generic.edit import FormView


from .models import Product, Product_types, Pulses, Salt, Salt_products, Meat, Meat_products, Pulses, Pulses_products
# Create your views here.

class IndexView(generic.ListView):
    template_name = 'produce/index.html'
    context_object_name = 'latest_product_list'
    # paginate_by = 15  # that is all it takes to add pagination in a Class Based View

    def get_queryset(self):
        return Product.objects.all()

class DetailView(generic.DetailView, generic.FormView):
    model = Product
    template_name = 'produce/detail.html'
    # context_object_name = 'product_types_list'
    form_class = ProductForm
    succes_url = "produce"

    # https://docs.djangoproject.com/en/3.2/topics/class-based-views/generic-editing/
    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)

    def get_queryset(self):
        return Product.objects.all()


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