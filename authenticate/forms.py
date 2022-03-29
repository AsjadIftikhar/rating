from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    """Provide a view for creating users with only the requisite fields."""

    class Meta:
        model = User
        # Note that password is taken care of for us by auth's UserCreationForm.
        fields = ('username', 'email')

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True
