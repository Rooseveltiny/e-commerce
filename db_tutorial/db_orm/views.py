from django.shortcuts import render
from django.http import HttpResponse
from .push_xml import push_all
from .models import Product, Feature
from django.core.paginator import Paginator
from uuid import UUID
from django.db.models import Q

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
    all_features = set()
    for product in products_list:
        for feature in product.features_link.all():
            all_features.add(feature)

    feature_groups = set()
    for feature in all_features:
        feature_groups.add(feature.feature_group)

    groups_with_features = []
    for group in feature_groups:

        features_of_group = []
        for feature in all_features:
            if feature.feature_group == group:

                features_of_group.append(feature)

        group_element = {'name': group.name,
                         'features': features_of_group,
                         }

        groups_with_features.append(group_element)
    # end block

    filter_params = []
    if request.method == 'POST':

        filter_params = request.POST.getlist('filter_items')
        filter_params = [UUID(x) for x in filter_params]

        if len(filter_params):

            # collecting all features structured by group
            all_features = Feature.objects.filter(link__in=filter_params)
            all_groups = set([x.feature_group for x in all_features])

            groups_with_features1 = []
            for group in all_groups:

                collected_features_for_group = []
                for feature in all_features:
                    if feature.feature_group == group:
                        collected_features_for_group.append(feature)

                groups_with_features1.append(
                    {
                        'name': group.name,
                        'features': collected_features_for_group,
                    }
                )
            # end block

            for element in groups_with_features1:
                products_list = products_list.filter(
                    features_link__in=element['features'])

            # products_list = list(dict.fromkeys(products_list))

    context = {'products': products_list,
               'groups_with_features': groups_with_features,
               'filter_params': filter_params,
               }

    return render(request, 'catalog.html', context=context)
