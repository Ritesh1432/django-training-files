from django.shortcuts import render

# Create your views here.
def example_view(request):
    # create my_app/templates/my_app/home.html
    return render(request,'my_app/home.html')

def variable_view(request):
    my_var = {
    'first_name':'Ritesh','last_name':'Dewoolkar',
    'some_list':['Ritesh','Franklin','Rosalin'],
    'some_dict':{'uname1':'Ritesh1234','pass':'1234'},
    'num_dict':[1,2,3,4,'','List']
    }
    return render(request,"my_app/variable.html",context=my_var)