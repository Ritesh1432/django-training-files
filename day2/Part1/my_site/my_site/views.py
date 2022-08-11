from django.shortcuts import render

def index_view(request):
    return render(request,'index.html')

def my_custom_page_not_found_view(request,exception):
    return render(request,'404.html',status=404)