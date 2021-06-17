from django.urls import path

from .views import *

urlpatterns = [
    path('', IndexPageView.as_view(), name='index-page'),
    path('books/<slug:genre>/', BooksListView.as_view(), name='books-list'),
    path('books/details/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('create/', BookCreate.as_view(), name='create-book-url'),
    path('update/<int:pk>/', BookUpdate.as_view(), name='update-book-url'),
    path('delete/<int:pk>/', BookDelete.as_view(), name='delete-book-url'),
    path('search/', SearchResultsView.as_view(), name='search-results'),
    path('add_to_fav/<int:pk>', AddToFavList.as_view(), name='add-to-fav-list'),
    path('fav_list/', MyFavListView.as_view(), name='MyFavListView')


]
