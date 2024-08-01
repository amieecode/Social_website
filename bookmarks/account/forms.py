from django import forms
from django.contrib.auth import get_user_model

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='password', widget=forms.PasswordInput )
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput )

    class Meta:
        model = get_user_model()
        fields = ['username', 'first_name', 'email']

    def clean_passwords(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("passwords don't match.")
        return cd['password2']