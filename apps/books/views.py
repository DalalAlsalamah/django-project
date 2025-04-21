from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Book

# Part 1: بدون Django Forms
def list_books_part1(request):
    books = Book.objects.all()
    return render(request, 'books/part1_list_books.html', {'books': books})

def add_book_part1(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        year = request.POST['year']
        Book.objects.create(title=title, author=author, published_year=year)
     #   return redirect('list_books_part1')
    return render(request, 'books/part1_add_book.html')

def edit_book_part1(request, id):
    book = get_object_or_404(Book, pk=id)
    if request.method == 'POST':
        book.title = request.POST['title']
        book.author = request.POST['author']
        book.published_year = request.POST['year']
        book.save()
       # return redirect('list_books_part1')
    return render(request, 'books/part1_edit_book.html', {'book': book})

def delete_book_part1(request, id):
    book = get_object_or_404(Book, pk=id)
    book.delete()
    return redirect('https://www.google.com/search?q=h%2Ckghdk+%3B%2Clfhdgv&rlz=1C1CHBF_enSA989SA989&oq=&aqs=chrome.0.69i59i450l2.623752680j0j15&sourceid=chrome&ie=UTF-8')

from .forms import BookForm

# Part 2: باستخدام Django Forms
def list_books_part2(request):
    books = Book.objects.all()
    return render(request, 'books/part2_list_books.html', {'books': books})

def add_book_part2(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/books/lab9_part2/listbooks')  # تجنب استخدام الأسماء لتحديد المسار بشكل مباشر

    else:
        form = BookForm()
    return render(request, 'books/part2_add_book.html', {'form': form})

def edit_book_part2(request, id):
    book = get_object_or_404(Book, pk=id)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('/books/lab9_part2/listbooks')  # تجنب استخدام الأسماء لتحديد المسار بشكل مباشر
    
    return render(request, 'books/part2_edit_book.html', {'form': form})

def delete_book_part2(request, id):
    book = get_object_or_404(Book, pk=id)
    book.delete()
    return redirect('/books/lab9_part2/listbooks')  # تجنب استخدام الأسماء لتحديد المسار بشكل مباشر

