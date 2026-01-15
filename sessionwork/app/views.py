from django.shortcuts import render,HttpResponse,redirect
from .models import UserData
# Create your views here.

def set_session(request):
    request.session['username'] = 'Pratibha Rajawat'
    request.session['email'] = 'itclassindore@gmail.com'
    return HttpResponse("Session has been set")

def get_session(request):
    username = request.session.get('username')
    email = request.session.get('email')
    return HttpResponse(f"Username: {username}, Email: {email}")

def delete_session(request):
    try:
        del request.session['username']
        del request.session['email']
    except KeyError:
        pass
    return HttpResponse("Session data has been deleted")
