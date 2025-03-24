from django.urls import path
from . import views
from . import apps

urlpatterns = [
    path('', views.index, name="bookmodule.index"),  # الصفحة الرئيسية
    path('list_books/', views.list_books, name="bookmodule.list_books"),
    path('aboutus/', views.aboutus, name="bookmodule.aboutus"),
    path('<int:bookId>/', views.viewbook, name="bookmodule.view_one_book"), 
    path('links/', views.links, name="bookmodule.links"), 
path('formatting/', views.formatting, name="bookmodule.formatting"), 
path('listing/', views.listing, name="bookmodule.listing"), 
path('tables/', views.tables, name="bookmodule.tables"), 
path('search/', views.search, name="bookmodule.search"), 
 path('simple/query', views.search, name="simple_query"), 
 path('complex/query', views.search, name="complex_query"), 
]