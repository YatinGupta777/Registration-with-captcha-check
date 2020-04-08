from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from ipware import get_client_ip
from .forms import *
from .models import User,IpCount
from django.http import JsonResponse
import requests
from django.conf import settings
from django.contrib import messages
import datetime


def signup(request):

    ip, is_routable = get_client_ip(request)
    invalid = False
    
    #When the user visit the page or reloads it
    try:
        counter = IpCount.objects.get(ip_address=ip)
        if(counter.last_date != datetime.date.today() and counter.count < 4):
            counter.last_date = datetime.date.today()
            counter.count = 0
            counter.save()
    except IpCount.DoesNotExist:
        counter = IpCount()
        counter.ip_address = ip
        counter.last_date = datetime.date.today()
        counter.save()
        
    
    html_ip_address = counter.ip_address
    html_count = counter.count            
    
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        
        if form.is_valid():
            
            counter = IpCount.objects.get(ip_address=ip)
            html_ip_address = counter.ip_address
            html_count = counter.count       
            
            if(counter.count > 3):
                ''' Begin reCAPTCHA validation '''
                recaptcha_response = request.POST.get('g-recaptcha-response')
                data = {
                    'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                    'response': recaptcha_response
                }
                r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
                result = r.json()
                ''' End reCAPTCHA validation '''
                
                if result['success']:
                    form.save()
                    return redirect('success')
                else:
                    invalid = True
                    return render(request, 'signup.html', {'form': form,"html_ip_address":html_ip_address,"html_count":html_count,"invalid":invalid})
            else:
                form.save()
                return redirect('success')    
               # return render(request, 'signup.html', {'form': form,"html_ip_address":html_ip_address,"html_count":html_count,"invalid":invalid})

    else:
        form = SignUpForm()
        
    return render(request, 'signup.html', {'form': form,"html_ip_address":html_ip_address,"html_count":html_count,"invalid":invalid})

def success(request):
    return render(request, 'success.html')

#When user try to register
def registration_attempt(request):
    ip, is_routable = get_client_ip(request)
    try:
        counter = IpCount.objects.get(ip_address=ip)
        counter.count = counter.count+1
        counter.save()
    except IpCount.DoesNotExist:
        counter = IpCount()
        counter.ip_address = ip
        counter.last_date = datetime.date.today()
        counter.save()
    
    html_ip_address = counter.ip_address
    html_count = counter.count        
    data = {
        'html_ip_address': html_ip_address, "html_count":html_count
    }
    return JsonResponse(data)        
