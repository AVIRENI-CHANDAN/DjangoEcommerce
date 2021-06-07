from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def demoPage(req):
    return render(req,'admin_templates/base_template.html')

def demoPageTemplate(req):
    return render(req,'demo.html')

def adminLogin(req):
    return render(req,'admin_templates/signin.html')