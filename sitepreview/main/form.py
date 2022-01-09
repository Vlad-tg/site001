from django import forms
from django.contrib.auth.models import User
from .models import *


class LoginForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Username'
        self.fields['password'].label = 'Password'

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        if not User.objects.filter(username=username).exists():
            raise forms.ValidationError(f'User with login {username} not found in the system.')
        user = User.objects.filter(username=username).first()
        if user:
            if not user.check_password(password):
                raise forms.ValidationError("Invalid password")
        return self.cleaned_data

    class Meta:
        model = User
        fields = ['username', 'password']


class RegistrationForm(forms.ModelForm):

    email = forms.EmailField(required=False)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    phone = forms.CharField(required=False)
    address = forms.CharField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].label = 'First name'
        self.fields['last_name'].label = 'Last name'
        self.fields['username'].label = 'Username'
        self.fields['email'].label = 'Email'
        self.fields['password'].label = 'Password'
        self.fields['confirm_password'].label = 'Confirm password'
        self.fields['phone'].label = 'Phone'
        self.fields['address'].label = 'Address'

    def clean(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError(f'Password mismatch')
        return self.cleaned_data

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(f'The {username} is taken')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        marks = email.split('.')[-1]
        if marks in ['net']:
            raise forms.ValidationError(f'Registration with such marks "{marks}" is not possible')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(f'The e-mail address is registered in the system')
        return email

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password', 'confirm_password', 'phone', 'address']


class TestForm(forms.ModelForm):
    title = forms.CharField(initial='Title product')
    country = forms.ChoiceField(required=False)
    pub_date = forms.CharField(widget=forms.TextInput(attrs={'size': '40'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].label = 'Title'
        self.fields['country'].label = 'Country'
        self.fields['pub_date'].label = 'Pub date'

    class Meta:
        model = Product
        fields = ['title', 'country', 'pub_date']

