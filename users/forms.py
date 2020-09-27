from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class StudentCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, widget=forms.TextInput(
        attrs={'id': 'first_name', 'class': 'form-control', 'placeholder': 'first name'}))
    fathers_name = forms.CharField(max_length=20, widget=forms.TextInput(
        attrs={'id': 'fathers_name', 'class': 'form-control', 'placeholder': "father's name"}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'id': 'last_name', 'class': 'form-control', 'placeholder': 'last name'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'id': 'username', 'class': 'form-control', 'placeholder': 'username eg (jhon16)'}))
    std = forms.IntegerField(max_value=10, min_value=8, widget=forms.NumberInput(
        attrs={'id': 'std', 'class': 'form-control stu-info', 'placeholder': 'std'}))
    div = forms.CharField(max_length=1, widget=forms.TextInput(
        attrs={'id': 'div', 'class': 'form-control stu-info', 'placeholder': 'division'}))
    rollno = forms.IntegerField(
        widget=forms.NumberInput(attrs={'id': 'rollno', 'class': 'form-control stu-info', 'placeholder': 'roll no'}))
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'id': 'email', 'class': 'form-control', 'placeholder': 'email'}))
    password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={'id': 'password1', 'class': 'form-control', 'placeholder': 'password'}))
    password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={'id': 'password2', 'class': 'form-control', 'placeholder': 'confirm password'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'std', 'div', 'rollno', 'email', 'password1', 'password2']


class TeacherCreatinForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, widget=forms.TextInput(
        attrs={'id': 'first_name', 'class': 'form-control', 'placeholder': 'first name'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'id': 'last_name', 'class': 'form-control', 'placeholder': 'last name'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'id': 'username', 'class': 'form-control', 'placeholder': 'username eg (jhon16)'}))
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'id': 'email', 'class': 'form-control', 'placeholder': 'email'}))
    password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={'id': 'password1', 'class': 'form-control', 'placeholder': 'password'}))
    password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={'id': 'password2', 'class': 'form-control', 'placeholder': 'confirm password'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']