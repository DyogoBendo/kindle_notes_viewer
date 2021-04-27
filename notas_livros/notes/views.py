from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Book, Note
from .forms import NotesForm, NoteForm
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .file_handler import handle_txt_file

# Create your views here.


class BookListView(ListView):
    model = Book
    template_name = 'home.html'


class BookNotesListView(ListView):
    model = Note
    template_name = 'notas_livro.html'
    
    def get_queryset(self):
        return Note.objects.filter(
            book = self.kwargs['book']
        )



class BookCreateView(CreateView):
    model = Book
    template_name = 'add_livro.html'
    fields = '__all__'    



def get_notes(request, book=None):
    if request.method == 'POST':        
        form = NotesForm(request.POST, request.FILES)        
        if form.is_valid():
            print("Post: ", request.POST)
            print("File: ", request.FILES)
            print('Pré: ', form)
            data =  handle_txt_file(request.FILES['notes_file'])                        

            post = request.POST.copy()
            for d in data:                                
                post['posicao_inicial'] = d['posicao_inicial']
                post['posicao_final'] = d['posicao_final']
                post['data'] = d['data']                
                post['nota'] = d['nota']
                post['destaque'] = d['destaque']                

                form = NoteForm(post)
                if form.is_valid():      
                    print("Passou:", post)              
                    form.save()
                else:
                    print('Deu ruim:', post)

            return HttpResponseRedirect('/')
    
    else:                
        form = NotesForm()        
        form.fields["book"].initial = book        
    
    return render (request, 'add_notas_livro.html', {'form': form})
