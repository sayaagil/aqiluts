from django.shortcuts import render

def index(request):
    return render(request,'hotel/index.html')

# Create your views here.
