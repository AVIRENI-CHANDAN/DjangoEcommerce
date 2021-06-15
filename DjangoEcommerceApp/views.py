from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import AnonymousUser
from django.contrib import messages
from django.urls import reverse

# Create your views here.
def index(req):
    return HttpResponseRedirect(reverse('adminHome'))
    
def demoPage(req):
    return HttpResponse("Working Demo")

def demoPageTemplate(req):
    return render(req,'demo.html')

def adminLogin(req):
    is_authenticated_user = authenticate(req.user)
    print("\nIs authenticated user:",is_authenticated_user,end="\n\n")
    print("\n\nThe present user is:",req.user,end="\n\n")
    print("The present user is not AnonymousUser:",(req.user.__str__() is not "AnonymousUser"),end="\n\n")
    print(req.user.__str__())
    # if is_authenticated_user:
    if (req.user.__str__() != "AnonymousUser") and (req.user != None):
        print("The user is autheticated to enter the adminHome")
        return HttpResponseRedirect(reverse('adminHome'))
    return render(req,'admin_templates/signin.html')

def adminLoginProcess(req):
    try:
        username = req.POST['username']
        password = req.POST['password']
    except:
        return HttpResponseRedirect(reverse('Admin Login'))
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