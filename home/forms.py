from django.forms import ModelForm, FileField, TextInput
from isbn_field import ISBNField
from home.models import PDFBook


class BookForm(ModelForm):
    class Meta:
        model = PDFBook
        fields = ['pdf']

        widgets = {
            # 'isbn': TextInput(attrs=({'class': 'form-control mb-2'})),
            # 'pdf': FileField(attrs=({'class': 'form-control'}))
        }
