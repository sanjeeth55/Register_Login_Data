from django import forms


class LoginForm(forms.Form):
    identifier = forms.CharField(label='Username or Email', max_length=250)
    password = forms.CharField(widget=forms.PasswordInput)