from .catalog_filter import get_groups_with_features, filter_products
from django.core.paginator import Paginator
from django.http import HttpResponse
from .models import Product, Feature
from django.shortcuts import render
from .push_xml import push_all
from django.db.models import Q
from uuid import UUID

# Create your views here


def load_data(request):

    push_all()
    return HttpResponse('ok')

def contacts(request):

    return render(request, 'contacts.html')

def main_page(request):

    return render(request, 'index.html')

def information(request):

    return render(request, 'information.html')

# query list of products and perform a structure of filter

def catalog(request):

    catalog_link = request.get_full_path()
    products_list = Product.objects.all()

    # gets data for filter from products
    groups_with_features = get_groups_with_features(products_list)

    filter_params = request.GET.getlist('filter_items')
    filter_params = [UUID(x) for x in filter_params]

    if len(filter_params):

        # filter products according to the given params from a form
        products_list = filter_products(filter_params, products_list)
 
    quantity_of_products = len(products_list)

    # pagination block
    paginator = Paginator(products_list, 8)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)
    is_paginated = page.has_other_pages()

    if page.has_previous():
        previous_page_number = page.previous_page_number()
    else:
        previous_page_number = ''

    if page.has_next():
        next_page_number = page.next_page_number()
    else:
        next_page_number = ''


    context = {
               'products': page,
               'groups_with_features': groups_with_features,
               'filter_params': filter_params,
               'is_paginated': is_paginated,
               'next_page_number': next_page_number,
               'previous_page_number': previous_page_number,
               'quantity_of_products': quantity_of_products,
               }

    return render(request, 'catalog.html', context=context)


