from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from authapp.models import ShopUser

class LoginForm(AuthenticationForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'password')


    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

        # modify each input field in form
        # to <input class='form-control'
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class RegisterForm(UserCreationForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'age', 'password1', 'password2', 'email', 'first_name')

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''  # clean help_text to make form look more fancy


class UpdateForm(UserChangeForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'age', 'password', 'email', 'first_name')

    def __init__(self, *args, **kwargs):
        super(UpdateForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''

        if field_name ==  'password':
            field.widget = forms.HiddenInput()
