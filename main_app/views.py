from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('<h1>RECORDS HERE</h1>')

def about(request):
    return render(request, 'about.html')

def records_index(request):
  return render(request, 'records/index.html', { 'records': records })
