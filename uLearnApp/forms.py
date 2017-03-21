from django import forms

class RegisterForm(forms.ModelForm):
        email = forms.CharField(widget = forms.EmailInput(attrs={'class': 'required form-control', 'placeholder': 'Email*'}),label = '')
        name = forms.CharField(widget = forms.TextInput(attrs={'class': 'required form-control', 'placeholder': 'Name*'}),label = '')
        surname = forms.CharField(widget = forms.TextInput(attrs={'class': 'required form-control', 'placeholder': 'Surname*'}),label = '')
        password = forms.CharField(widget = forms.PasswordInput(attrs={'class': 'required form-control', 'placeholder': 'Password*'}),label = '')
        conform_password = forms.CharField(widget = forms.PasswordInput(attrs={'class': 'required form-control', 'placeholder': 'Conform password*'}),label = '')
        bdate = forms.CharField(widget = forms.TextInput(attrs={'type':'date','class':'required form-control','id':'exampleInputDOB1'}),label = '')
