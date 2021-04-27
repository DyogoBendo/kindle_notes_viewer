from django.urls import path

from .views import BookListView, BookNotesListView, BookCreateView, get_notes

urlpatterns = [
    path('', BookListView.as_view(), name='home'),
    path('book-notes/<int:book>', BookNotesListView.as_view(), name='notas-livro'),    
    path('book/new/', BookCreateView.as_view(), name='add_book'), 
    path('book/notes/new/(?P<book>[0-9]+)$  ', get_notes, name='add_notes')
]