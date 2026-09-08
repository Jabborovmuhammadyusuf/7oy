from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Category, Book, Comment
from .forms import BookForm


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


def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id, published=True)
    comments = Comment.objects.filter(book_id=book_id).order_by('-created')
    context = {"book": book, "comments": comments}
    return render(request, "main/book_detail.html", context)


def create_book(request):
    if request.user.is_staff:
        if request.method == "POST":
            form = BookForm(data=request.POST, files=request.FILES)
            if form.is_valid():
                book = form.save()
                messages.success(request, "Kitob muvaffaqiyatli qo'shildi!")
                return redirect("book_detail", book_id=book.id)
        else:
            form = BookForm()
        context = {"form": form}
        return render(request, "main/book_form.html", context)
    else:
        return redirect("all_books")


def update_book(request, book_id):
    if request.user.is_staff:
        book = get_object_or_404(Book, pk=book_id)
        if request.method == "POST":
            form = BookForm(data=request.POST, files=request.FILES, instance=book)
            if form.is_valid():
                form.save()
                messages.success(request, "Muvaffaqiyatli o'zgartirildi!")
                return redirect("book_detail", book_id=book.id)
        else:
            form = BookForm(instance=book)
        context = {"form": form, "book": book}
        return render(request, "main/book_form.html", context)
    else:
        return redirect('all_books')


def delete_book(request, book_id):
    if request.user.is_superuser:
        book = get_object_or_404(Book, pk=book_id)
        if request.method == 'POST':
            book.delete()
            messages.success(request, "Kitob muvaffaqiyatli o'chirildi!")
            return redirect('all_books')
        else:
            return render(request, "main/book_confirm_delete.html", {"book": book})
    else:
        return redirect('all_books')
