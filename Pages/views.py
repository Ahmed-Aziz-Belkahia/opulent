from django.shortcuts import render

# Create your views here.

def index1(request, *args, **kwargs):
    return render(request, "index.html", {})

def index1(request, *args, **kwargs):
    return render(request, "runok\index.html", {})

def index2(request, *args, **kwargs):
    return render(request, "runok\index-2.html", {})

def index3(request, *args, **kwargs):
    return render(request, "runok\index-3.html", {})

def index4(request, *args, **kwargs):
    return render(request, "runok\index-4.html", {})

def index5(request, *args, **kwargs):
    return render(request, "runok\index-5.html", {})

def index6(request, *args, **kwargs):
    return render(request, "runok\index-6.html", {})