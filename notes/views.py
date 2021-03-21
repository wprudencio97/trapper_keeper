from django.shortcuts import render, redirect
from django.views.generic import DetailView, UpdateView, DeleteView
from .models import Note
from .forms import NoteForm

# Create your views here.


class NoteDetailView(DetailView):
    model = Note
    template_name = 'note_detail.html'

class NoteUpdateView(UpdateView):
    model = Note
    template_name = 'note_form.html'
    fields = ['note_title', 'note_content'] 

class NoteDeleteView(DeleteView):
    model = Note
    success_url = '/'

def notes(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('notes')
    else:
        form = NoteForm()
        notes = Note.objects.all().order_by('-date_created')
        context = {
            'notes':notes,
            'form':form
        }
    return render(request, 'notes.html', context)