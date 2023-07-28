from django.shortcuts import render

# Create your views here.


def index(request):
    # read the Database
    # create context variable (dict)
    my_dict = {'pages': ['one', 'two', 'three', 'four'],
               'courses': ['frontend', 'backend']}
    return render(request, 'myapp/index.html', context=my_dict)


def home(request):
    return render(request, 'myapp/home.html')
