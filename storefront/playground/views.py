from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def say_hello(request):
    # Pull data from db
    # Transform
    # Send email and so on...

    return render(request, 'hello.html', {'name':'Aunim'})