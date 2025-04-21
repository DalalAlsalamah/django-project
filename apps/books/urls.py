from django.urls import path
from . import views

urlpatterns = [
    # Part 1 (بدون Django forms)
    path('lab9_part1/listbooks', views.list_books_part1, name='list_books_part1'),
    path('lab9_part1/addbook', views.add_book_part1, name='add_book_part1'),
    path('lab9_part1/editbook/<int:id>', views.edit_book_part1, name='edit_book_part1'),
    path('lab9_part1/deletebook/<int:id>', views.delete_book_part1, name='delete_book_part1'),

    # Part 2 (باستخدام Django forms)
    path('lab9_part2/listbooks', views.list_books_part2, name='list_books_part2'),
    path('lab9_part2/addbook', views.add_book_part2, name='add_book_part2'),
    path('lab9_part2/editbook/<int:id>', views.edit_book_part2, name='edit_book_part2'),
    path('lab9_part2/deletebook/<int:id>', views.delete_book_part2, name='delete_book_part2'),
]

