import traceback

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from authenticate.decorators import authenticated_user
from django.contrib.auth import logout
from django.contrib import messages
import PyPDF2
import io

from .forms import BookForm
from .helpers import *


# Login Page Controller
@authenticated_user
def home(request):
    words = []
    percentage = 0.0
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():

            try:
                file = request.FILES['pdf'].read()
                file = PyPDF2.PdfFileReader(io.BytesIO(file))
                content = ""
                for i in range(file.numPages):
                    text = file.getPage(i)
                    content += text.extractText()

                words = remove_stopwords(content)
                percentage = probability(words)
                messages.success(request, "Successful")
                # form.save()
            except Exception as ex:
                messages.error(request, "Something Went WRONG. Please Upload correct PDF File!")

        context = {'user': request.user,
                   'form': form,
                   'total_words': len(words),
                   'percentage': float("{:.2f}".format(percentage))}
        return render(request, 'home/book.html', context)
    else:
        form = BookForm()
        context = {'user': request.user,
                   'form': form}
        return render(request, 'home/home.html', context)


def user_history(request):
    return render(request, 'home/history.html', {'heading': "History"})


def all_books(request):
    return render(request, 'home/history.html', {'heading': "Library"})


@authenticated_user
def log_out(request):
    logout(request)
    return redirect('/login')
