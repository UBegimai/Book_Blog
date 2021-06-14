from django.shortcuts import render

from main.models import Genre

def index(request):
    return render(request, 'index.html')
    # genres = Genre.objects.all()
    # return render(request, 'index.html', {'genres': genres})

# def book_list(request, slug):
#     books = Book.objects.filter(genre__slug=slug)
#     return render(request, )