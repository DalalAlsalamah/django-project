from django import forms
from .models import Student, Address, Student2, Address2, Gallery

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email']

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['student', 'city', 'street']

class Student2Form(forms.ModelForm):
    class Meta:
        model = Student2
        fields = ['name', 'email']

class Address2Form(forms.ModelForm):
    class Meta:
        model = Address2
        fields = ['students', 'city', 'street']

class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ['title', 'image']


from django import forms
from .models import StudentImage

class StudentImageForm(forms.ModelForm):
    class Meta:
        model = StudentImage
        fields = ['student', 'image']
