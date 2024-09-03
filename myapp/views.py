from django.shortcuts import render


def index(request):
    return render(request, 'index.html', context=dict(text='Hello world'))