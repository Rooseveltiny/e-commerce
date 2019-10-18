from .models import Feature, FeatureGroup, Product
import xml.etree.ElementTree as ET

def push_feature_group():

    tree = ET.parse('/home/saveliy/projects/exp/FeaturesGroup.xml')
    root = tree.getroot()

    for child in root:

        element = FeatureGroup(name = child.attrib['name'], link = child.attrib['uuid']) 
        element.save()

def push_feature():

    tree = ET.parse('/home/saveliy/projects/exp/Features.xml')
    root = tree.getroot() 

    for child in root:

        element = Feature(name = child.attrib['name'],
         link = child.attrib['uuid'], 
         feature_group_id = child.attrib['feature_group_uuid'])

        element.save()

def push_product():

    tree = ET.parse('/home/saveliy/projects/exp/Products.xml')
    root = tree.getroot()
    # root = ET.fromstring(tree)

    for child in root:
        
        element = Product(name = child.attrib['name'],
        link = child.attrib['uuid'], 
        price = make_a_float(child.attrib['price']),
        unit_of_measurement = child.attrib['unit_of_measurement'],
        balance = make_a_float(child.attrib['balance']))

        element.save() 

        element.features_link.set([])  

        for item in child.find('features').findall('item'):

            element.features_link.add(item.attrib['feature'])

       


def make_a_float(value: str) -> float:

    value = value.replace(' ','')
    value = value.replace('\xa0', '')
    value = float(value.replace(',','.'))
    return value    


def push_all():

    push_feature_group()
    push_feature()
    push_product()
