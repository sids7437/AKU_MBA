from django.shortcuts import render
from .models import Faculty, Notice, Event


def home(request):

    faculties = Faculty.objects.all()
    notices = Notice.objects.all().order_by('-date')
    events = Event.objects.all().order_by('-date')

    return render(request, 'home.html', {
        'faculties': faculties,
        'notices': notices,
        'events': events
    })


def faculty(request):

    faculties = Faculty.objects.all()

    return render(request, 'faculty.html', {
        'faculties': faculties
    })


def notices(request):

    notices = Notice.objects.all().order_by('-date')

    return render(request, 'notices.html', {
        'notices': notices
    })

def events(request):

    events = Event.objects.all().order_by('-date')

    return render(request, 'events.html', {
        'events': events
    })

def about(request):

    return render(request, 'about.html')

def programme(request):

    return render(request, 'programme.html')

def contact(request):

    return render(request, 'contact.html')