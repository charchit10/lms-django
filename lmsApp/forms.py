from datetime import datetime
from sys import prefix
from django import forms
from numpy import require
from lmsApp import models
import datetime

class SaveBook(forms.ModelForm):
    isbn = forms.CharField(max_length=250)
    title = forms.CharField(max_length=250)
    description = forms.Textarea()
    author = forms.Textarea()
    publisher = forms.Textarea()
    date_published = forms.DateField()
    status = forms.CharField(max_length=2)

    class Meta:
        model = models.Books
        fields = ('isbn', 'title', 'description', 'author', 'publisher', 'date_published', 'status', )

    def clean_isbn(self):
        id = int(self.data['id']) if (self.data['id']).isnumeric() else 0
        isbn = self.cleaned_data['isbn']
        try:
            if id > 0:
                book = models.Books.objects.exclude(id = id).get(isbn = isbn, delete_flag = 0)
            else:
                book = models.Books.objects.get(isbn = isbn, delete_flag = 0)
        except:
            return isbn
        raise forms.ValidationError("ISBN already exists on the Database.")
    
class SaveStudent(forms.ModelForm):
    code = forms.CharField(max_length=250)
    first_name = forms.CharField(max_length=250)
    middle_name = forms.CharField(max_length=250, required= False)
    last_name = forms.CharField(max_length=250)
    gender = forms.CharField(max_length=250)
    contact = forms.CharField(max_length=250)
    email = forms.CharField(max_length=250)
    department = forms.CharField(max_length=250)
    course = forms.CharField(max_length=250)
    address = forms.Textarea()
    status = forms.CharField(max_length=2)

    class Meta:
        model = models.Students
        fields = ('code', 'first_name', 'middle_name', 'last_name', 'gender', 'contact', 'email', 'address', 'department', 'course', 'status', )

    def clean_code(self):
        id = int(self.data['id']) if (self.data['id']).isnumeric() else 0
        code = self.cleaned_data['code']
        try:
            if id > 0:
                book = models.Books.objects.exclude(id = id).get(code = code, delete_flag = 0)
            else:
                book = models.Books.objects.get(code = code, delete_flag = 0)
        except:
            return code
        raise forms.ValidationError("Student School Id already exists on the Database.")
    
class SaveBorrow(forms.ModelForm):
    student = forms.CharField(max_length=250)
    book = forms.CharField(max_length=250)
    borrowing_date = forms.DateField()
    return_date = forms.DateField()
    status = forms.CharField(max_length=2)

    class Meta:
        model = models.Borrow
        fields = ('student', 'book', 'borrowing_date', 'return_date', 'status', )

    def clean_student(self):
        student = int(self.data['student']) if (self.data['student']).isnumeric() else 0
        try:
            student = models.Students.objects.get(id = student)
            return student
        except:
            raise forms.ValidationError("Invalid student.")
            
    def clean_book(self):
        book = int(self.data['book']) if (self.data['book']).isnumeric() else 0
        try:
            book = models.Books.objects.get(id = book)
            return book
        except:
            raise forms.ValidationError("Invalid Book.")
