from django.shortcuts import render
from .models import Record
from django.views.generic.edit import CreateView, UpdateView, DeleteView
<<<<<<< HEAD
from .forms import SongForm
=======

>>>>>>> 32f0a0296d1484c6f0d64eaf8a78e2c3c09839e9
# Create your views here.

class RecordCreate(CreateView):
    model = Record
    fields = '__all__'

class RecordUpdate(UpdateView):
    model = Record
    fields = ['release_year', 'genre', 'review']

class RecordDelete(DeleteView):
    model = Record
    success_url = '/records/'

<<<<<<< HEAD

=======
    
>>>>>>> 32f0a0296d1484c6f0d64eaf8a78e2c3c09839e9
def home(request):
    return render('<h1>RECORDS HERE</h1>')

def about(request):
    return render(request, 'about.html')

def records_index(request):
    records = Record.objects.all()
    return render(request, 'records/index.html', { 'records': records })

def records_detail(request, record_id):
    record = Record.objects.get(id=record_id)
<<<<<<< HEAD
    song_form = SongForm()
    return render(request, 'records/detail.html', {'record': record, 'song_form': song_form})
=======
    return render(request, 'records/detail.html', {'record': record})
>>>>>>> 32f0a0296d1484c6f0d64eaf8a78e2c3c09839e9

