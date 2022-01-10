from django.db import models

# Create your models here.
class Hostel(models.Model):
    hotel_name = models.CharField(max_length=50100)
    price = models.IntegerField()
    room_number = models.CharField(max_length=10000)
    tel_no = models.CharField(default='nonumber', max_length=10000)
    adres = models.CharField(max_length=10000)
    hlatitude = models.CharField(max_length=100000)
    hlongitude = models.CharField(max_length=10000)
    rank = models.FloatField(max_length=10000)
    hotel_link = models.CharField(max_length=10000)
