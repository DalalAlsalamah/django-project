from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from django.db import models

from django.db.models import Q, Count, Sum, Avg, Max, Min
from django.shortcuts import render
from .models import Book, Student, Address

def index(request):
    return render(request, "bookmodule/index.html")
 
def list_books(request):
    return render(request, 'bookmodule/list_books.html')

def aboutus(request):
    return render(request, 'bookmodule/aboutus.html')
 
def viewbooks(request, booksId):
    return render(request, 'bookmodule/one_books.html')
    
def links(request):
    return render(request, 'bookmodule/links.html')
def formatting(request):
    return render(request, 'bookmodule/formatting.html')
def listing(request):
    return render(request, 'bookmodule/listing.html')
def tables(request):
    return render(request, 'bookmodule/tables.html')

def search(request):

    if request.method == "POST":
        string = request.POST.get('keyword').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')
    

        # now filter
        books = __getbooksList()
        newbooks = []
        for item in books:
            contained = False
            if isTitle and string in item['title'].lower(): contained = True
            if not contained and isAuthor and string in item['author'].lower():contained = True
            
            if contained: newbooks.append(item)
        return render(request, 'bookmodule/booksList.html', {'books':newbooks})
    return render(request, 'bookmodule/search.html')


def __getbooksList():
    books1 = {'id':12344321, 'title':'Continuous Delivery', 'author':'J.Humble and D. Farley'}
    books2 = {'id':56788765,'title':'Reversing: Secrets of Reverse Engineering', 'author':'E. Eilam'}
    books3 = {'id':43211234, 'title':'The Hundred-Page Machine Learning books', 'author':'Andriy Burkov'}
    return [books1, books2, books3]

def task1_view(request):
   books =Book.objects.filter(Q(price__lte=80))
   return render(request, 'bookmodule/task1.html', {'books': books})

def task2_view(request):
   books = Book.objects.filter(
      Q(edition__gt=3) & (Q(title__icontains='co') | Q(authors__icontains='co'))
   )
   return render(request, 'bookmodule/task2.html', {'books': books})

def task3_view(request):
   books = Book.objects.filter(
      ~Q(edition__gt=3) & ~(Q(title__icontains='co') | Q(authors__icontains='co'))
   )
   return render(request, 'bookmodule/task3.html', {'books': books})

def task4_view(request):
   books = Book.objects.all().order_by('title')
   return render(request, 'bookmodule/task4.html', {'books': books})

def task5_view(request):
   stats = Book.objects.aggregate(
      total_books=Count('id'),
      total_price=Sum('price'),
      avg_price=Avg('price'),
      max_price=Max('price'),
      min_price=Min('price')
   )
   return render(request, 'bookmodule/task5.html', {'stats': stats})
from django.shortcuts import render
from django.db.models import Count
from .models import Address

def task7_view(request):
    # استخدام annotate لحساب عدد الطلاب في كل مدينة
    city_stats = Address.objects.annotate(student_count=Count('student'))
    
    return render(request, 'bookmodule/task7.html', {'city_stats': city_stats})
