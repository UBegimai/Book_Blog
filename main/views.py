
from django.contrib import messages
from django.core import paginator
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import *

from .forms import BookForm, CommentForm
from .models import *

def books_list(request):
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    is_paginated = page.has_other_pages()

    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''

    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''

    context = {
        'page_object': page,
        'is_paginated': is_paginated,
        'next_url': next_url,
        'prev_url': prev_url
    }


    return render(request, 'main/index.html', context=context)


class IndexPageView(View):
    def get(self, request):
        genres = Genre.objects.all()
        books = Book.objects.all()
        return render(request, 'main/index.html', locals())


class BooksListView(ListView):
    queryset = Book.objects.all()
    template_name = 'main/books-list.html'
    context_object_name = 'books'
    paginate_by = 4

    def get_queryset(self):
        queryset = super().get_queryset()
        genre_id = self.kwargs.get('genre')
        return queryset.filter(genre_id=genre_id)


class BookDetailView(DetailView):
    queryset = Book.objects.all()
    template_name = 'main/book-detail.html'
    context_object_name = 'book'


class BookCreate(CreateView):
    queryset = Book.objects.all()
    template_name = 'main/create-book.html'
    form_class = BookForm


class BookUpdate(UpdateView):
    model = Book
    template_name = 'main/update-book.html'
    form_class = BookForm


class BookDelete(DeleteView):
    model = Book
    template_name = 'main/delete-book.html'
    success_url = reverse_lazy('home')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        messages.add_message(request, messages.SUCCESS, 'Successfully deleted')
        return HttpResponseRedirect(success_url)

def book_detail(request, pk):
    book = get_object_or_404(Book, id=pk)
    # List of active comments for this book
    comments = book.comment.filter(active=True)

    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current book to the comment
            new_comment.book = book
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request,
                  'main/comment-add.html',
                  {'book': book,
                   'comments': comments,
                   'comment_form': comment_form})

class SearchResultsView(View):
    def get(self, request):
        q = request.GET.get('q', '')
        if q:
            books = Book.objects.filter(Q(title__icontains=q))
        else:
            books = Book.objects.none()
        return render(request, 'main/search.html', {'books': books})


class AddToFavList(View):
    def get(self, request, pk):
        book = get_object_or_404(Book, id=pk)
        FavoriteBooks.objects.create(book=book, user=request.user)
        return redirect('/ibook/fav_list/')


class MyFavListView(View):
    def get(self, request):
        user = request.user
        books_ids = user.favorites.values('book_id')
        books = Book.objects.filter(id__in=books_ids)
        return render(request, 'main/fav_list.html', context={'books': books})
















