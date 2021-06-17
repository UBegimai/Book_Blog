
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import *

from .forms import BookForm
from .models import *

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





















# class PostDetail(ObjectDetailMixin, View):
#     model = Post
#     template = 'blog/post_detail.html'
#
# class PostCreate(LoginRequiredMixin, ObjectCreateMixin, View):
#     model_form = PostForm
#     template = 'blog/post_create_form.html'
#     raise_exception = True
#
# class PostUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
#     model = Post
#     model_form = PostForm
#     template = 'blog/post_update_form.html'
#     raise_exception = True
#
# class PostDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
#     model = Post
#     template = 'blog/post_delete_form.html'
#     redirect_url = 'posts_list_url'
#     raise_exception = True