from django.shortcuts import render,redirect
from django.urls import reverse
from . import models
from .forms import ReviewForm

# Create your views here.
def rental_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            form.save()
            return redirect(reverse('Cars:thankyou'))
    else:
        form = ReviewForm()
    return render(request,'Cars/rentalreview.html',context={'form':form})

def thank_you(request):
    return render(request,'Cars/thankyou.html')
