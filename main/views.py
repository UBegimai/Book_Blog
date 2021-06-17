import django_filters
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import modelformset_factory
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
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
    paginate_by = 3

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


# class BookDelete(DeleteView):
#     model = Book
#     template_name =






















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