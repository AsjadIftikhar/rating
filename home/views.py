from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from authenticate.decorators import authenticated_user
from django.contrib.auth import logout
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
            file = request.FILES['pdf'].read()
            file = PyPDF2.PdfFileReader(io.BytesIO(file))
            content = ""
            for i in range(file.numPages):
                text = file.getPage(i)
                content += text.extractText()

            print(content)
            words = remove_stopwords(content)
            percentage = probability(words)
            # form.save()
        else:
            print("Invalid Form")
            print(form.errors)

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
def log_out(request):
    logout(request)
    return redirect('/login')
