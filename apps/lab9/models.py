from django.db import models

# Create your models here.
# models.py

from django.db import models

class Card(models.Model):
    card_number = models.IntegerField()

    def __str__(self):
        return str(self.card_number)


class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=100)
    code = models.IntegerField()

    def __str__(self):
        return f"{self.title} ({self.code})"


class Student(models.Model):
    name = models.CharField(max_length=100)
    
    # Part 1: One-to-One relation with Card (prevent delete)
    card = models.OneToOneField(Card, on_delete=models.PROTECT, null=True, blank=True)

    # Part 2: ForeignKey to Department (delete students if department deleted)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)

    # Part 3: ManyToMany with Course
    courses = models.ManyToManyField(Course, blank=True)

    def __str__(self):
        return self.name
