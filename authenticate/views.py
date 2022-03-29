import traceback

from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from authenticate.api import AudibleApi
from authenticate.audible_books import *
from authenticate.forms import RegistrationForm
from authenticate.speech_text import *
from home.helpers import *
from home.models import *
from authenticate.send_mail import *

# Sign Up Page Controller:
from home.models import Book


def register_page(request):
    """Default Django User Creation Form"""

    # form = UserCreationForm()
    form = RegistrationForm()

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
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
    # asin = asin[0:10]
    # print(asin)
    # print(title)
    if asin:
        try:
            find_books = Book.objects.get(ASIN=asin)
            (customer_history, created) = CustomerHistory.objects.get_or_create(
                user=request.user)
            find_books.customer_history.add(customer_history)
            context = {'user': request.user,
                       'total_sentences': find_books.total_words,
                       'percentage': find_books.profane_percentage,
                       'rating': find_books.rating
                       }

        except:

            try:
                auth = audible.Authenticator.from_file("cred.txt")
                client = audible.Client(auth=auth)
                download_book(auth=auth, client=client, asin=asin)
                book_text = speech_to_text(asin)

                (customer_history, created) = CustomerHistory.objects.get_or_create(
                    user_id=request.user)

                book_text_list = book_text.split('.')

                percentage, rating = probability(book_text_list)

                # save book
                new_book = Book(ASIN=asin, title=title, rating=rating, total_words=len(book_text_list),
                                profane_percentage=percentage)
                new_book.save()
                new_book.customer_history.add(customer_history)

                # send email
                sendMail("The requested rating for the book " + title + " is " + rating)

                context = {'user': request.user,
                           'total_sentences': len(book_text_list),
                           'percentage': float("{:.2f}".format(percentage)),
                           'rating': rating
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
