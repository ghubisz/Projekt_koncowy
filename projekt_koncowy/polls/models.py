import datetime

import dateutil.utils
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


#Klasa Category ma za zadanie wyświetlić jedynie nazwę Kategorii, która jest połączona relacją jeden do wielu z Klasą Produkt.
#Bo każda kategoria może mieć wiele produktów ale produkt może mieć tylko jedną kategorię.
class Category(models.Model):
    name = models.CharField(max_length=128)
#    product = models.ManyToManyField(Product)

    def __str__(self):
        return self.name


#Klasa Product ma wyświetlać nazwę, opis, cenę jednostkową, ilość i kategorię przypisaną do produktu.
class Product(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



#Klasa data przydatności ma za zadanie wyświetlić wspomnianą datę, dla każdego pojedynczego produktu.
#Jest połączona relacją wiele do wielu z klasą Produkt, ponieważ data przydatności może występować nie tylko przy jednym produkcie.
class Expiration_Date(models.Model):
    expiration_date = models.DateField()
    product = models.ManyToManyField(Product)

    def __str__(self):
        return self.expiration_date


#Klasa Cena ma za zadanie wyświetlać cenę, która jest polem typu Float i ma przypisaną nazwę.
class Price(models.Model):
    name = models.CharField(max_length=128)
    price = models.FloatField()


#Klasa Shopping ma za zadanie wyświetlać listę zakupów, która jest tworzona na podstawie produktów zużytych (usuniętych).
class Shopping(models.Model):
    name = models.CharField(max_length=128)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    product_list = models.ManyToManyField(Product)
 #   price = models.ManyToManyField(Price)

    def __str__(self):
        return self.name


#Klasa History ma wyświetlać historię poprzednich zakupow, która generuje się na podstawie przyciku "Buy".
class History(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    arch_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


#Klasa Request ma wyświetlać nazwę, opis, ilość i kategorię przypisaną do produktu, na ktory ktos zglosil zapotrzebowanie.
class Requests(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    quantity = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    requestor = models.ForeignKey(User, on_delete=models.CASCADE)
    #cena?

    def __str__(self):
        return self.name
