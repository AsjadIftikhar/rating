import traceback

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from authenticate.decorators import authenticated_user
from django.contrib.auth import logout
from django.contrib import messages
import PyPDF2
import io

from .forms import BookForm
from .helpers import *
from .models import *


# Login Page Controller
@authenticated_user
def home(request):
    sentences = []
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

                print(content)
                # sentences = remove_stopwords(content)
                sentences = content.split('.')
                percentage, rating = probability(sentences)
                messages.success(request, "Successful")
                # form.save()
            except Exception as ex:
                messages.error(request, "Something Went WRONG. Please Upload correct PDF File!")
                print(traceback.format_exc())
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        context = {'user': request.user,
                   'form': form,
                   'total_sentences': len(sentences),
                   'percentage': float("{:.2f}".format(percentage)),
                   'rating': rating}
        return render(request, 'home/book.html', context)
    else:
        form = BookForm()
        context = {'user': request.user,
                   'form': form}
        return render(request, 'home/home.html', context)


@authenticated_user
def user_history(request):
    context = {}
    if request.method == 'GET':
        (customer_history, created) = CustomerHistory.objects.get_or_create(
            user=request.user)
        if customer_history.books.exists():
            list_books = Book.objects.all()
            context = {'heading': 'History',
                       'all_books': list_books}

        return render(request, 'home/history.html', context)


@authenticated_user
def all_books(request):
    if request.method == 'GET':
        list_books = Book.objects.all()
        context = {'heading': 'Library',
                   'all_books': list_books}
        return render(request, 'home/history.html', context)


@authenticated_user
def log_out(request):
    logout(request)
    return redirect('/login')
