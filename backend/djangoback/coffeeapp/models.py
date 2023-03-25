from django.db import models

# Create your models here.
class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
'''
class Site(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
'''

class City(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)

class MetroStation(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    longitude = models.FloatField()
    latitude = models.FloatField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)

class Address(models.Model):
    id = models.AutoField(primary_key=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    street = models.CharField(max_length=64)
    building_number = models.CharField(max_length=8)
    longitude = models.FloatField()
    latitude = models.FloatField()
    metro_station = models.ForeignKey(MetroStation, on_delete=models.CASCADE)
    #description = models.CharField(max_length=128) #comment


class CoffeeShop(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=128)
    picture = models.URLField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag) # многие ко многим
    link = models.URLField()
    comment = models.CharField(max_length=128)

#links = models.ManyToManyField(Site, through='Link') # многие ко многим
'''
# связующая таблица, где хранится ссылка на конкретный сайт
class Link(models.Model):
    id = models.AutoField(primary_key=True)
    coffee_shop = models.ForeignKey(CoffeeShop, on_delete=models.CASCADE)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    linkString = models.URLField()
'''