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


from django.http import HttpResponse

def set_cookies(request):
    response = HttpResponse("Cookies have been set")
    # Cookie set with 1 hour expiry, HttpOnly for security
    response.set_cookie(
        key='username',
        value='itclassindore',
        max_age=3600,       # seconds
        
    )
    return response  # IMPORTANT: yahi response return karo

def get_cookies(request):
    username = request.COOKIES.get('username')  # safe get
    if username:
        return HttpResponse(f"Username from cookies: {username}")
    else:
        return HttpResponse("No cookies found")

def delete_cookies(request):
    response = HttpResponse("Cookies have been deleted")
    response.delete_cookie('username')
    return response  # IMPORTANT: yahi response return karo

def visiter_track(request):
    if 'visits' in request.COOKIES:
        visits = int(request.COOKIES['visits']) + 1
    else:
        visits = 1
    response = HttpResponse(f"Number of visits: {visits}")
    response.set_cookie('visits', str(visits), max_age=365*24*60*60)  # 1 year
    return response
