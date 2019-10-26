from django.db import models
import uuid

# Create your models here.

class Simple(models.Model):

    text = models.CharField(max_length=10)
    number = models.IntegerField(null=True)
    url = models.URLField(default='www.example.com')

    def __str__(self):

        return self.url

class DateExample(models.Model):

    the_date = models.DateTimeField()


class NullExample(models.Model):

    col = models.CharField(max_length=10, blank=True, null=True)

class Language(models.Model):

    name = models.CharField(max_length=10)

    def __str__(self):

        return self.name

class Framework(models.Model):

    name = models.CharField(max_length=10)
    language = models.ForeignKey('Language', on_delete=models.CASCADE)

    def __str__(self):

        return self.name


class Movie(models.Model):

    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Character(models.Model):

    name = models.CharField(max_length=10)
    movies = models.ManyToManyField(Movie)

    def __str__(self):

        return self.name


class FeatureGroup(models.Model):

    link = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)

class Feature(models.Model):

    name = models.CharField(max_length=50)
    link = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    feature_group = models.ForeignKey('FeatureGroup', on_delete = models.CASCADE, default = None)

    def __repr__(self):
        return repr((self.name, self.link, self.feature_group))

class Product(models.Model):

    link = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    unit_of_measurement = models.CharField(max_length=10, default=None)
    balance = models.DecimalField(max_digits=15, decimal_places=3, default=0)
    features_link = models.ManyToManyField(Feature)




    
