from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request) : 
    developed_by = "Sourav Kumar"
    mentors = [
        "Sourav Kumar",
        "Jitesh Kumar Singh",
        "krishna"
    ]
    context = {
        "developers" : developed_by ,
        "mentors" : mentors     
    }
    response = render(request,'HelloWorld/index.html',context)
    return response 