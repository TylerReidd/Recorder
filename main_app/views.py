from django.shortcuts import render

from .models import Record
# Create your views here.

records = [
    Record('Aja', 1977, 'jazz-rock?', 'A reaally good album'),
    Record('blue', 1977, 'folk-jazz?', 'pretty good album. Good color'),
    Record('Sail Away', 1970, 'rock', 'one of the best')
]


def home(request):
    return render('<h1>RECORDS HERE</h1>')

def about(request):
    return render(request, 'about.html')

def records_index(request):
    return render(request, 'records/index.html', { 'records': records })
