from django import forms

class InputForm(forms.Form):
    x=forms.IntegerField(label='enter 1st number')
    y=forms.IntegerField(label='enter 2nd number')


class RegisterForm(forms.Form):
    email=forms.EmailField(label='enter your email here')
    password = forms.CharField(widget=forms.PasswordInput, label='enter your password here')
    confirm_password = forms.CharField(widget=forms.PasswordInput, label='confirm your password')

class CompleteForm(forms.Form):
    age=forms.IntegerField(label='enter your age')
    weight=forms.IntegerField(label='enter your weight')
    height=forms.IntegerField(label='enter your height')
    goal=forms.IntegerField(label='enter your ideal weight goal')


class LoginForm(forms.Form):
    email=forms.EmailField(label='enter your email here')
    password = forms.CharField(widget=forms.PasswordInput, label='enter your password here')



    