from django.db import models
from datetime import datetime
from realtors.models import Realtor

class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING, verbose_name='Pośrednik')
    title = models.CharField(max_length=200, verbose_name='Tytuł')
    address = models.CharField(max_length=200, verbose_name='Adres')
    city = models.CharField(max_length=100, verbose_name='Miasto')
    province = models.CharField(max_length=100, verbose_name="Województwo")
    zipcode = models.CharField(max_length=20, verbose_name='Kod pocztowy')
    description = models.TextField(blank=True, verbose_name='Opis')
    price = models.IntegerField(verbose_name='Cena')
    bedrooms = models.IntegerField(verbose_name='Sypialnie')
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1, verbose_name='Łazienki')
    garage = models.IntegerField(default=0, verbose_name='Garaże')
    sqmeters = models.IntegerField(default=0, verbose_name='Metry kwadratowe')
    lot_size = models.DecimalField(max_digits=5, decimal_places=1, verbose_name='Wielkość')
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Główne Zdjęcie')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Dodatkowe wnetrza 1')
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Dodatkowe wnetrza 2')
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Dodatkowe wnetrza 3')
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Dodatkowe wnetrza 4')
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Dodatkowe wnetrza 5')
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Dodatkowe wnetrza 6')
    is_published = models.BooleanField(default=True, verbose_name='Opublikowany')
    list_date = models.DateTimeField(default=datetime.now, blank=True, verbose_name='Data')
    def __str__(self):
        return self.title
