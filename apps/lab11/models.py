from django.db import models

# Task 1: OneToOne Relation
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Address(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.city}, {self.street}"

# Task 2: ManyToMany Relation
class Student2(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Address2(models.Model):
    students = models.ManyToManyField(Student2)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.city}, {self.street}"

# Task 3: Table with Images
class Gallery(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title



class StudentImage(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='student_images/')

    def __str__(self):
        return f"صورة للطالب: {self.student.name}"
