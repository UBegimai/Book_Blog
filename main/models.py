from django.db import models

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

class Book(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    published = models.DateField()
    image = models.ImageField(blank=True, null=True, upload_to='books')
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title

