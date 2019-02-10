from django import forms
from django.contrib.auth.forms import AuthenticationForm

from authapp.models import CustomUser

class LoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password')


    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

        # modify each input field in form
        # to <input class='form-control'
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
