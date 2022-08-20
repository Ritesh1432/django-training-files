from django import forms
from .models import Review
from django.forms import ModelForm

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
        labels = {
            'first_name':'First Name',
            'last_name':'Last Name',
            'stars':'Rating'
        }
        error_messages = {
            'stars':{
                'min_value':"Minimum value should be 1",
                'max_value':'Max value should be 5'
            }
        }

    # first_name = forms.CharField(label="First Name",max_length=100)
    # last_name = forms.CharField(label="Last Name",max_length=100)
    # email = forms.EmailField(label="Email")
    # review = forms.CharField(label="Please write your feedback here")
    # review.widget.attrs.update({'class':'form-control'})
    # first_name.widget.attrs.update({'class':'form-control'})
    # last_name.widget.attrs.update({'class':'form-control'})
    # email.widget.attrs.update({'class':'form-control'})