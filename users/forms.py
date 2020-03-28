from django.forms import ModelForm
from django import forms
from .models import Users, Document, Searches
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

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document', 'user')
        user = forms.ModelMultipleChoiceField(queryset=Users.objects.none(), widget=forms.CheckboxSelectMultiple())
        widgets = {
            'description': forms.TextInput(attrs={'class':'form-control', 'maxlength':255}),
            'document': forms.FileInput(attrs={'class':'form-control', 'maxlength':255}),

        }

class SearchForm(forms.ModelForm):
    class Meta:
        model = Searches
        fields = ('result', 'user')
        user = forms.ModelMultipleChoiceField(queryset=Users.objects.none(), widget=forms.CheckboxSelectMultiple())
        widgets = {
            'result': forms.Textarea(attrs={'class':'form-control'}),

        }