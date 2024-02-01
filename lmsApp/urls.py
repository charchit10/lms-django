from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.books, name="book-page"),
    path('books',views.books,name='book-page'),
    path('manage_book',views.manage_book,name='manage-book'),
    path('manage_book/<int:pk>',views.manage_book,name='manage-book-pk'),
    path('view_book/<int:pk>',views.view_book,name='view-book-pk'),
    path('save_book',views.save_book,name='save-book'),
    path('delete_book/<int:pk>',views.delete_book,name='delete-book'),
    path('students',views.students,name='student-page'),
    path('manage_student',views.manage_student,name='manage-student'),
    path('manage_student/<int:pk>',views.manage_student,name='manage-student-pk'),
    path('view_student/<int:pk>',views.view_student,name='view-student-pk'),
    path('save_student',views.save_student,name='save-student'),
    path('delete_student/<int:pk>',views.delete_student,name='delete-student'),
    path('borrows',views.borrows,name='borrow-page'),
    path('manage_borrow',views.manage_borrow,name='manage-borrow'),
    path('manage_borrow/<int:pk>',views.manage_borrow,name='manage-borrow-pk'),
    path('view_borrow/<int:pk>',views.view_borrow,name='view-borrow-pk'),
    path('save_borrow',views.save_borrow,name='save-borrow'),
    path('delete_borrow/<int:pk>',views.delete_borrow,name='delete-borrow'),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
