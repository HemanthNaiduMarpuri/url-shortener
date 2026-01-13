from django import forms
from .models import Users

class UserSigninForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = Users
        fields = ('username', 'email', 'password')
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'})
        }

class UserLoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Enter Your Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Enter Your Password'}))
