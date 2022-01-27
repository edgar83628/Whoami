from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "EdgarWebsite/home.html")

def cover(request):
    return render(request, "EdgarWebsite/cover.html")

def resume(request):
    return render(request, "EdgarWebsite/resume.html")
