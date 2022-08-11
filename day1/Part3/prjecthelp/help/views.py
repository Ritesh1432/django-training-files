from django.shortcuts import render

# Create your views here.
def help_page_view(request):
    return render(request,'help/helpPage.html')

