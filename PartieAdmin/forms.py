from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


class NewUserForm(UserCreationForm):

    email = forms.EmailField(required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'class': 'input-group input-group-sm'}
        )
        self.fields['password1'].widget.attrs.update(
            {'class': 'input-group input-group-sm'}
        )
        self.fields['password2'].widget.attrs.update(
            {'class': 'input-group input-group-sm'}
        )
        self.fields['email'].widget.attrs.update(
            {'class': 'input-group input-group-sm'}
        )

    class Meta:
        model = User
        fields = ("username","email","password1","password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        if commit:
            user.save()
        return user


class CustomLoginForm(AuthenticationForm):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['username'].widget.attrs.update(
      {'class': 'input-group input-group-sm'}
    )
    self.fields['password'].widget.attrs.update(
      {'class': 'input-group input-group-sm'}
    )