from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=False, help_text='Required',
                                 widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Username'}))
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional',
                                 widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'First name'}))
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional',
                                 widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Last name'}))
    email = forms.CharField(max_length=254, help_text='Required. Inform a valid email address',
                              widget=forms.EmailInput({
                                   'class': 'form-control',
                                   'placeholder': 'Email Address'}))
    password1 = forms.CharField(max_length=254, help_text='Required',
                              widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder': 'Password'}))
    password2 = forms.CharField(max_length=254, help_text='Required',
                              widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

    def save(self, commit = True):
        user = super(SignUpForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user
