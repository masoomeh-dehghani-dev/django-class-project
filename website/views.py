from django.shortcuts import render

# Create your views here.

def test(request):
    return render(request,'website/test.html')

def about(request):
    return render(request,'website/about.html')

def contact(request):
    return render(request,'website/contact.html')

def elements(request):
    return render(request,'website/elements.html')

def index(request):
    return render(request,'website/index.html')
