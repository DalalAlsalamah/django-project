from django.urls import path
from . import views

urlpatterns = [
    # Task 1
    path('students/', views.student_list, name='student_list'),
    path('students/add/', views.student_add, name='student_add'),
    path('students/update/<int:pk>/', views.student_update, name='student_update'),
    path('students/delete/<int:pk>/', views.student_delete, name='student_delete'),

    # Task 2
    path('students2/', views.student2_list, name='student2_list'),
    path('students2/add/', views.student2_add, name='student2_add'),

    # Task 3
    path('gallery/', views.gallery_list, name='gallery_list'),
    path('gallery/add/', views.gallery_add, name='gallery_add'),

      path('upload/', views.upload_image, name='upload_image'),
    path('images/', views.image_list, name='image_list'),
]
