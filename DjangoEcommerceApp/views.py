from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.urls import reverse

# Create your views here.
def demoPage(req):
    return HttpResponse("Working Demo")

def demoPageTemplate(req):
    return render(req,'demo.html')

def adminLogin(req):
    return render(req,'admin_templates/signin.html')

def adminLoginProcess(req):
    username = req.POST['username']
    password = req.POST['password']
    user = authenticate(request=req,username=username,password=password)
    if user is not None:
        login(request=req,user=user)
        return HttpResponseRedirect(reverse('adminHome'))
    else:
        messages.error(req,"Error in login! Invalid credentials")
        return HttpResponseRedirect(reverse('Admin Login'))

def adminLogoutProcess(req):
    logout(req)
    messages.success(req,"Sucessfully logged out!")
    return HttpResponseRedirect(reverse('Admin Login'))