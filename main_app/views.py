from django.shortcuts import render, redirect
from .models import Record, Photo
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import SongForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
import uuid 
import boto3

# Create your views here.
S3_BASE_URL = 'https://s3.us-east-1.amazonaws.com/'
BUCKET = 'recordcollector00'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

def add_photo(request, record_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            photo = Photo(url=url, record_id=record_id)
            photo.save()
        except:
            print('An error occured uploading file to s3')
        return redirect('detail', record_id=record_id)

class RecordCreate(CreateView):
    model = Record
    fields = ['artist', 'title', 'genre', 'release_year', 'review']
    
    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class RecordUpdate(UpdateView):
    model = Record
    fields = ['release_year', 'genre', 'review']

class RecordDelete(DeleteView):
    model = Record
    success_url = '/records/'

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def records_index(request):
    records = Record.objects.filter(user=request.user)
    return render(request, 'records/index.html', { 'records': records })

@login_required
def records_detail(request, record_id):
    record = Record.objects.get(id=record_id)
    song_form = SongForm()        
    return render(request, 'records/detail.html', {'record': record, 'song_form': song_form})

@login_required
def add_song(request, record_id):
    form = SongForm(request.POST)
    if form.is_valid():
        new_song = form.save(commit=False)
        new_song.record_id = record_id
        new_song.save()
    return redirect('detail', record_id=record_id)



