from .models import Feature

def get_groups_with_features(products_list):

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

        group_element = {
                        'name': group.name,
                        'features': features_of_group,
                         }

        groups_with_features.append(group_element)

    return groups_with_features

def filter_products(filter_params, products_list):

    all_features = Feature.objects.filter(link__in=filter_params)
    all_groups = set([x.feature_group for x in all_features])

    groups_with_features = []
    for group in all_groups:

        collected_features_for_group = []
        for feature in all_features:
            if feature.feature_group == group:
                collected_features_for_group.append(feature)

        groups_with_features.append(
                    {
                        'name': group.name,
                        'features': collected_features_for_group,
                    }
                )

    for element in groups_with_features:
        products_list = products_list.filter(
            features_link__in=element['features'])

    return products_list