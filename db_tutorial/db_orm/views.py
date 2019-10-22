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

    # gets data for filter
    groups_with_features = get_groups_with_features(products_list)

    filter_params = []
    if request.method == 'POST':

        filter_params = request.POST.getlist('filter_items')
        filter_params = [UUID(x) for x in filter_params]

        if len(filter_params):

            # gets filtered catalog according to filter params
            products_list = filter_products(filter_params, products_list)

    paginator = Paginator(products_list, 1)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    is_paginated = page.has_other_pages()

    if page.has_previous():
        previous_url = '?page={}'.format(page.previous_page_number())
    else:
        previous_url = ''

    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''


    context = {'products': page,
               'groups_with_features': groups_with_features,
               'filter_params': filter_params,
               'is_paginated': is_paginated,
               'next_url': next_url,
               'previous_url': previous_url,
               }

    return render(request, 'catalog.html', context=context)
