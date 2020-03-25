from django.forms import ModelForm
from django import forms
from .models import Users

class UserModelForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['username','first_name','last_name','CPF','RG','Endereço', 'email','password']
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control', 'maxlength':255}),
            'last_name': forms.TextInput(attrs={'class':'form-control', 'maxlength':255}),
            'Endereço': forms.TextInput(attrs={'class':'form-control', 'maxlength':255}),
            'CPF': forms.TextInput(attrs={'class':'form-control', 'maxlength':11}),
            'RG': forms.TextInput(attrs={'class':'form-control', 'maxlength':9}),
            'username': forms.TextInput(attrs={'class':'form-control', 'maxlength':255}),
            'email': forms.TextInput(attrs={'class':'form-control', 'maxlength':255}),
            'password': forms.PasswordInput(attrs={'class':'form-control', 'maxlength':255}),
        }