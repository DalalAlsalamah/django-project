from django.shortcuts import render
from django.db.models import Count, Min
from .models import Department, Course, Student
from django.db.models import Min, Subquery, OuterRef

def task1(request):
    departments = Department.objects.annotate(student_count=Count('student'))
    
    return render(request, 'lab9/task1.html', {'departments': departments})

def task2(request):
    courses = Course.objects.annotate(student_count=Count('student'))
    return render(request, 'lab9/task2.html', {'courses': courses})

def task3(request):

    departments = Department.objects.annotate(
        oldest_student_id=Min('student__id')  
    )

    for dept in departments:

        oldest_student = Student.objects.filter(id=dept.oldest_student_id).first()
        dept.oldest_student_name = oldest_student.name if oldest_student else "No student"

    return render(request, 'lab9/task3.html', {'departments': departments})

def task4(request):
    departments = Department.objects.annotate(student_count=Count('student')).filter(student_count__gt=2).order_by('-student_count')
    return render(request, 'lab9/task4.html', {'departments': departments})
 
 
 
 
 

