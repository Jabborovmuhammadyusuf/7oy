from django.urls import path
from .views import all_books, boks_by_category, book_detail, create_book, update_book, delete_book

urlpatterns=[
    path('', all_books, name='all_books'),
    path('category/<int:category_id>/', boks_by_category, name='books_by_category'),
    path('book/<int:book_id>/', book_detail, name='book_detail'),
    path('book/add/', create_book, name='add_book'),
    path('book/<int:book_id>/update/', update_book, name='book_update'),
    path('book/<int:book_id>/delete/', delete_book, name='book_delete'),
]