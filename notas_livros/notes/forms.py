from django import forms
from django.db.models import fields
from .models import Note

class NotesForm(forms.Form):
    book = forms.IntegerField(label="Id do Livro")
    notes_file = forms.FileField(label="Arquivo com notas")


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('book', 'nota', 'data', 'posicao_inicial', 'posicao_final', 'destaque')
    

"""    book = forms.IntegerField(label="Id do Livro")
    posicao_inicial = forms.IntegerField()
    posicao_final = forms.IntegerField()
    destaque = forms.Textarea()
    data = forms.DateField()
    nota = forms.Textarea()"""