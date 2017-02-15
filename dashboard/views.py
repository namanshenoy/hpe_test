from django.shortcuts import render

# Create your views here.


def index(request):
    print 'rendering'
    return render(request, 'index.html')
