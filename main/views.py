import django_filters
from django.forms import modelformset_factory
from django.shortcuts import render
from django.views.generic import *
from django_filters import FilterSet

from .models import *

class IndexPageView(View):
    def get(self, request):
        genres = Genre.objects.all()
        books = Book.objects.all()
        return render(request, 'main/index.html', locals())

# # class BooksFilterSet(FilterSet):
# #     author = django_filters.CharFilter('author__email',
# #                                        lookup_expr='iexact')
# #     created_at = django_filters.DateFilter('created_at',
# #                                            lookup_expr='gt')
# #
# #     class Meta:
# #         model = Book
# #         fields = ['tags', 'author']
#
# class BooksListView(ListView):
#     queryset = Book.objects.all()
#     template_name = 'main/books_list.html'
#     context_object_name = 'books'
#     paginate_by = 3
#
#     def get_queryset(self):
#         queryset = super().get_queryset()
#         genre_id = self.kwargs.get('genre')
#         return queryset.filter(genre_id=genre_id)
#
#     # def get_context_object_name(self, *,object_list=None, **kwargs):
#     #     context = super().get_context_data()
#     #     filter = BooksFilterSet(self.request.GET,
#     #                             queryset = self.get_queryset())
#     #     context['filter'] = filter
#     #     return context
#
# class GenreDetailView(DetailView):
#     model = Genre
#     template_name = 'genre-detail.html'
#     context_object_name = 'genre'
#
#     def get(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         self.slug = kwargs.get('slug', None)
#         return super().get(request, *args, **kwargs)
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['books'] = Book.objects.filter(genre_id=self.slug)
#         return context
#
# class BookDetailView(DetailView):
#     model = Book
#     template_name = 'book-detail.html'
#     context_object_name = 'book'
#
















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