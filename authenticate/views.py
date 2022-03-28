import traceback

from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from authenticate.api import AudibleApi
from authenticate.audible_books import *
from authenticate.speech_text import *
from home.helpers import *
from home.models import *

# Sign Up Page Controller:
from home.models import Book


def register_page(request):
    """Default Django User Creation Form"""

    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('loginPage')

    context = {'form': form}
    return render(request, 'authenticate/register.html', context)


# Login Page Controller
def login_page(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')

        user = authenticate(request, username=name, password=password)

        if user:
            login(request, user)
            return redirect('/home/')
        else:
            messages.info(request, 'Username OR password Incorrect')
            return redirect('loginPage')

    context = {}
    return render(request, 'authenticate/login.html', context)


# Login Page Controller
def audible_login(request, asin="", title=""):
    context = {}
    if asin:
        try:
            find_books = Book.objects.get(ASIN=asin)
            (customer_history, created) = CustomerHistory.objects.get_or_create(
                user=request.user)
            customer_history.books.add(find_books)
            #find_books.save()
            context = {'user': request.user,
                       'total_words': len(find_books.profane_words),
                       'percentage': float("{:.2f}".format(find_books.profane_percentage))
                       }
        except:

            try:
                auth = audible.Authenticator.from_file("cred.txt")
                client = audible.Client(auth=auth)
                # download_book(auth=auth, client=client, asin=asin)
                book_text = speech_to_text()

                words = remove_stopwords(book_text)
                percentage = probability(words)

                (customer_history, created) = CustomerHistory.objects.get_or_create(
                    user=request.user)
                customer_history.books.add(find_books)

                #save book
                new_book = Book(ASIN=asin, title=title, rating="temp", customer_history=customer_history)
                new_book.save()
                context = {'user': request.user,
                           'total_words': len(words),
                           'percentage': float("{:.2f}".format(percentage))
                           }
            except Exception as ex:
                messages.info(request, traceback.format_exc())

        return render(request, 'home/book.html', context)
    else:
        library = None
        try:
            api = AudibleApi()
            client = api.get_client()
            library = api.get_library()
            api.de_register()

            messages.success(request, "Successfully Linked Audible Account")

            context = {'library': library['items']}
            print(library['items'])
            return render(request, 'authenticate/audible.html', context)
        except Exception as ex:
            messages.error(request, "Failed to Login Audible")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def page_not_found(request):
    return render(request, 'authenticate/404.html', {})
