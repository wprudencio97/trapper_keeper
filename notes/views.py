from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Note
from .forms import NoteForm

# Create your views here.

notes = {
    'Note1': 'This is note 1.',
    'Note2': 'This is note 2.',
    'Note3': 'This is note 3'
}



class NoteListView(ListView):
    model = Note
    template_name = 'index.html'
    context_object_name = 'notes'


def index(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        form.save()
        return redirect('index')
    else:
        notes = Note.objects.all
        context = {
            'notes':notes
        }


    return render(request, 'index.html', context)