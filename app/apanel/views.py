from django.shortcuts import render
from .forms import fileForm
from django.views.generic.edit import FormView

def index(request):
    return render(request, "index.html")


def upload(request):
    return render(request, "project.html")


def uploadFile(request):
    if request.method == 'POST':
        form = fileForm(request.POST, request.FILES)
        files=[]
        if form.is_valid():
            form.save()
            f1 = open('data.txt')
            res = f1.read()
            files.append(res)
            return render(request, 'project.html', {'files':files})
    else:
        form = fileForm
    return render(request, 'index.html', {'form':form})