from django.shortcuts import render
from django.http import HttpResponse
from .push_xml import push_all
from .models import Product

# Create your views here


def load_data(request):

    push_all()
    return HttpResponse('ok')


def main_page(request):

    return render(request, 'index.html')

# query list of products and perform a structure of filter


def catalog(request):

    products_list = Product.objects.all()


    ### block that forms group of features_groups with features just to make a filter
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
                         'features': features_of_group}

        groups_with_features.append(group_element)
    ### end block


    context = {'products': products_list,
               'groups_with_features': groups_with_features}

    return render(request, 'catalog.html', context=context)
