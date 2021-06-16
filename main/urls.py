from django.urls import path

from .views import *

urlpatterns = [
    path('', IndexPageView.as_view(), name='home'),
    path('books/<slug:genre>/', BooksListView.as_view(), name='books-list'),
    path('books/details/<int:pk>/', BookDetailView.as_view(), name='book-detail'),




]
