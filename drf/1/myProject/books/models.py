from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255, primary_key = True)
    author = models.CharField(max_length=255)
    publication_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return f'title: {self.title} author: {self.author} publication date: {self.publication_date} description: {self.description}'