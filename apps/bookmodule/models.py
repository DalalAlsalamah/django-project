from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=50)
    authors = models.CharField(max_length=50)
    price = models.FloatField(default=0.0)
    edition = models.SmallIntegerField(default=1)

    class Meta:
       db_table = "books"


class Address(models.Model):
    city = models.CharField(max_length=100)


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
 

 