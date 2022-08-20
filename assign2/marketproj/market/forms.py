from dataclasses import fields
from urllib import request
from django import forms
from .models import User
from django.forms import ModelForm



class RegisterForm(forms.ModelForm):
    cpw = forms.CharField(label="Confirm Password",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ('username','emailid','budget','password')
        widgets = {
            'password':forms.PasswordInput(attrs={'class':'form-control'}),
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'emailid':forms.EmailInput(attrs={'class':'form-control'}),
            'budget':forms.NumberInput(attrs={'class':'form-control'})
            }
    def clean(self):
        cleaned_data = super(RegisterForm,self).clean()
        pw = cleaned_data.get('password')
        cpw = cleaned_data.get('cpw')
        if(pw != cpw):
            raise forms.ValidationError("Password and Confirm Password did not match")
        return cleaned_data


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','password')
        widgets = {
            'password':forms.PasswordInput(attrs={'class':'form-control'}),
            'username':forms.TextInput(attrs={'class':'form-control'})
        }


