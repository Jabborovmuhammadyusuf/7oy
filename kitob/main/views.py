from django.shortcuts import render
from .models import Category,Book

def all_books(request):
    category=Category.objects.all()
    book=Book.objects.filter(published=True)
    context={
        'categoryes': category,
        'books': book
}
    return render(request,'main/all_books.html',context)

def boks_by_category(request,category_id):
    books=Book.objects.filter(category_id=category_id,published=True)
    categoryes=Category.objects.all()
    context={
        'books':books,
        'categoryes':categoryes,
    }
    return render(request,'main/all_books.html',context)