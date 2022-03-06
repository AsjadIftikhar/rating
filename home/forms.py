from django.forms import ModelForm, FileField, TextInput
from isbn_field import ISBNField
from home.models import Book


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['pdf']

        widgets = {
            # 'isbn': TextInput(attrs=({'class': 'form-control mb-2'})),
            # 'pdf': FileField(attrs=({'class': 'form-control'}))
        }
