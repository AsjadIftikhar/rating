import traceback

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from rest_framework.response import Response
from authenticate.decorators import authenticated_user
from django.contrib.auth import logout
from django.contrib import messages
import PyPDF2
import io

from .forms import BookForm
from .helpers import *
from .models import Books


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
                messages.info(request, "Successful")
                # form.save()
            except Exception as ex:
                messages.info(request, traceback.format_exc())

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


@authenticated_user
def user_history(request):
    if request.method == 'GET':
        current_user = request.user
        if current_user.customerhistory.books.exists():
            list_books = Books.objects.all()
            context = {'heading': 'history',
                       'user_all_books': list_books}
            return render(request, 'home/home.html', context)



@authenticated_user
def all_books(request):
    if request.method == 'GET':
        list_books = Books.objects.all()
        context = {'heading': 'history',
                   'all_books': list_books}
        return render(request, 'home/home.html', context)


# get history list of books
# history = Books.objects.all
# .filter blank
# request.user,

# 1 user 1 hist

@authenticated_user
def log_out(request):
    logout(request)
    return redirect('/login')
