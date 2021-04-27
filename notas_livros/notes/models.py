from django.db import models
from django.urls import reverse

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    capa = models.ImageField(upload_to="book_cover/")
    isbn = models.CharField(max_length=15)

    def __str__(self) -> str:
        return self.title


    def get_absolute_url(self):        
        # args = dict()
        # args["book"] = self.id                
        return reverse('add_notes', args=[str(self.id)])


class Note(models.Model):    
    posicao_inicial = models.IntegerField()
    posicao_final = models.IntegerField()
    destaque = models.TextField()
    data = models.CharField(max_length=200)
    nota = models.TextField(null=True)
    book = models.ForeignKey('Book', on_delete=models.CASCADE, default=0)

    def __str__(self) -> str:
        book = self.book
        inicio = self.posicao_inicial
        fim = self.posicao_final
        txt = f'{book}: {inicio} - {fim}'
        return txt