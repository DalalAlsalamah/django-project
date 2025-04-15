from django.urls import path 
from django.urls import include
from . import views
from . import apps

urlpatterns = [
    path('', views.index, name="bookmodule.index"),  # الصفحة الرئيسية
    path('list_books/', views.list_books, name="bookmodule.list_books"),
    path('aboutus/', views.aboutus, name="bookmodule.aboutus"),
    path('<int:bookId>/', views.viewbooks, name="bookmodule.view_one_book"), 
    path('links/', views.links, name="bookmodule.links"), 
    path('formatting/', views.formatting, name="bookmodule.formatting"), 
    path('listing/', views.listing, name="bookmodule.listing"), 
    path('tables/', views.tables, name="bookmodule.tables"), 
    path('search/', views.search, name="bookmodule.search"), 
    path('task1/', views.task1_view,name="bookmodule.task1"),
    path('task2/', views.task2_view),
    path('task3/', views.task3_view),
    path('task4/', views.task4_view),
    path('task5/', views.task5_view),
    path('task7/', views.task7_view),
   
]