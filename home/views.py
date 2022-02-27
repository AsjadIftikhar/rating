from django.core.files.storage import default_storage
from django.shortcuts import render
from .helperFunctions import *

# Login Page Controller
def home(request):
    context = {}
    return render(request, 'home/home.html', context)

# Upload Files
def uploadFiles(request):
    if request.method == 'POST':

        # here you get the files needed
        file = request.FILES['sentFile']
        fileContent = pdfToString(file)

        print(fileContent)


    context = {}
    return render(request, 'home/upload_files.html', context)

