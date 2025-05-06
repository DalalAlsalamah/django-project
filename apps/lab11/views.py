from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Address, Student2, Address2, Gallery
from .forms import StudentForm, AddressForm, Student2Form, Address2Form, GalleryForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
@login_required
def student_list(request):
    students = Student.objects.all()
    return render(request, 'lab11/student_list.html', {'students': students})
@login_required
def student_add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            # إضافة العنوان مباشرة بعد إضافة الطالب
            address_form = AddressForm(request.POST)
            if address_form.is_valid():
                address = address_form.save(commit=False)
                address.student = student  # ربط العنوان بالطالب
                address.save()
            return redirect('student_list')
    else:
        form = StudentForm()
        address_form = AddressForm()
    return render(request, 'lab11/student_form.html', {'form': form, 'address_form': address_form})

@login_required
def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'lab11/student_form.html', {'form': form})
@login_required
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'lab11/student_confirm_delete.html', {'student': student})

# Task 2 views
@login_required
def student2_list(request):
    students = Student2.objects.all()
    return render(request, 'lab11/student2_list.html', {'students': students})
@login_required
def student2_add(request):
    if request.method == 'POST':
        form = Student2Form(request.POST)
        if form.is_valid():
            student = form.save()
            # إضافة العناوين المرتبطة
            address_form = Address2Form(request.POST)
            if address_form.is_valid():
                address = address_form.save(commit=False)
                address.students.add(student)  # ربط الطالب بالعناوين
                address.save()
            return redirect('student2_list')
    else:
        form = Student2Form()
        address_form = Address2Form()
    return render(request, 'lab11/student2_form.html', {'form': form, 'address_form': address_form})


# Task 3 views (Gallery)
@login_required
def gallery_add(request):
    if request.method == 'POST':
        form = GalleryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gallery_list')
    else:
        form = GalleryForm()
    return render(request, 'lab11/gallery_form.html', {'form': form})
@login_required
def gallery_list(request):
    galleries = Gallery.objects.all()
    return render(request, 'lab11/gallery_list.html', {'galleries': galleries})

from django.shortcuts import render, redirect
from .forms import StudentImageForm
from .models import StudentImage
@login_required
def upload_image(request):
    if request.method == 'POST':
        form = StudentImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('image_list')
    else:
        form = StudentImageForm()
    return render(request, 'lab11/upload_image.html', {'form': form})
@login_required
def image_list(request):
    images = StudentImage.objects.all()
    return render(request, 'lab11/image_list.html', {'images': images})
