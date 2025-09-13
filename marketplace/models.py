from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    adress = models.CharField(max_length=200)
    number = models.CharField(max_length=10)

class Tovari(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    text = models.TextField()
    amount = models.IntegerField()
    date = models.DateField()
    image = models.ImageField('Изображение', upload_to='images/', blank=True, null=True, default='images/default.jpg')

class Korzina(models.Model):
    polzovatel = models.OneToOneField(User, on_delete=models.CASCADE, related_name='korzina')
    tovari = models.ManyToManyField(Tovari, related_name='korzini')








