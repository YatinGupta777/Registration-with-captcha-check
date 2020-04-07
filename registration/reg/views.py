from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from ipware import get_client_ip
from .forms import *
from .models import User,IpCount

def signup(request):
    ip, is_routable = get_client_ip(request)
    captcha = False
    try:
        counter = IpCount.objects.get(ip_address=ip)
        counter.count = counter.count+1
        counter.save()
        if(counter.count > 3):
            captcha = True
    except IpCount.DoesNotExist:
        counter = IpCount()
        counter.ip_address = ip
        counter.save()
                
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = SignUpForm()
        
    return render(request, 'signup.html', {'form': form, 'captcha':captcha})

def success(request):
    return render(request, 'success.html')


# =============================================================================
# def registration_attempt(request):
#     ip, is_routable = get_client_ip(request)
#     captcha = False
#     try:
#         counter = IpCount.objects.get(ip_address=ip)
#         counter.count = counter.count+1
#         counter.save()
#         if(counter.count > 3):
#             captcha = True
#     except IpCount.DoesNotExist:
#         counter = IpCount()
#         counter.ip_address = ip
#         counter.save()
#     data = {
#         'captcha': captcha
#     }
#     return JsonResponse(data)        
# =============================================================================
