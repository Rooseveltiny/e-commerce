from django.shortcuts import render
from django.http import HttpResponse
from .push_xml import push_all
from .models import Product, Feature
from django.core.paginator import Paginator
from uuid import UUID
from django.db.models import Q
from .catalog_filter import get_groups_with_features, filter_products

# Create your views here


def load_data(request):

    push_all()
    return HttpResponse('ok')


def main_page(request):

    return render(request, 'index.html')

# query list of products and perform a structure of filter


def catalog(request):

    products_list = Product.objects.all()

    # block that forms group of features_groups with features just to make a filter
    groups_with_features = get_groups_with_features(products_list)

    filter_params = request.GET.getlist('filter_items')
    filter_params = [UUID(x) for x in filter_params]

    if len(filter_params):

        products_list = filter_products(filter_params, products_list)

    context = {'products': products_list,
               'groups_with_features': groups_with_features,
               'filter_params': filter_params,
               }

    return render(request, 'catalog.html', context=context)
