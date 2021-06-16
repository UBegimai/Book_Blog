from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Author(models.Model):
    name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    date_of_birth = models.DateField()
    image = models.ImageField(blank=True, null=True,
                              upload_to='authors_image')
    def __str__(self):
        return f'{self.name} {self.last_name}'

class Genre(models.Model):
    slug = models.SlugField(primary_key=True, max_length=55)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Tag(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30, primary_key=True)

    def __str__(self):
        return self.title

class Book(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    published = models.DateField()
    image = models.ImageField(upload_to='books', blank=True, null=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='books')
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

    @property
    def get_image(self):
        return self.images.first()

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE,
                             related_name='comment')
    author_name = models.CharField(max_length=50)
    comment_text = models.TextField()
    published = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.comment_text

