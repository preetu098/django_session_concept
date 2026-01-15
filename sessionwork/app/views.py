from django.shortcuts import render,HttpResponse,redirect
from .models import UserData
# Create your views here.

def set_session(request,name):
    request.session['username'] = name
    request.session['email'] = 'itclassindore@gmail.com'
    return HttpResponse("Session has been set")

def get_session(request):
    if('username' not in request.session):
        return HttpResponse("No session data found")
    else:
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
