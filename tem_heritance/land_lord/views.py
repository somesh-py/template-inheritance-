from django.shortcuts import render

# Create your views here.

def parent(request):
    return render(request,'parent.html')

def frontend(request):
    return render(request,'frontend.html')

def backend(request):
    return render(request,'backend.html')