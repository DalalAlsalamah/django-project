from django.urls import path
from . import views
from . import apps

urlpatterns = [
    path('', views.index, name="bookmodule.index"),  # الصفحة الرئيسية
    path('list_books/', views.list_books, name="bookmodule.list_books"),
    path('aboutus/', views.aboutus, name="bookmodule.aboutus"),
    path('<int:bookId>/', views.viewbook, name="bookmodule.view_one_book"),  # وضعه في النهاية
]
