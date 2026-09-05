from django.urls import path
from .views import all_books,boks_by_category

urlpatterns=[
    path('',all_books, name='all_books'),
    path('category/<int:category_id>/',boks_by_category,name='books_by_category')
]