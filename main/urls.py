from django.urls import path

from .views import *

urlpatterns = [
    path('', IndexPageView.as_view(), name='home'),
    path('books/<slug:genre>/', BooksListView.as_view(), name='books-list'),
    path('books/details/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('create/', BookCreate.as_view(), name='create-book-url'),
    path('update/<int:pk>/', BookUpdate.as_view(), name='update-book-url'),
    path('delete/<int:pk>/', BookDelete.as_view(), name='delete-book-url'),


]
