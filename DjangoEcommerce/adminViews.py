from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.contrib.messages.views import SuccessMessageMixin,messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.storage import FileSystemStorage
from django.urls import reverse
from django.http import HttpResponseRedirect

from DjangoEcommerceApp.models import Categories,SubCategories,MerchantUser,CustomUser

@login_required
def admin_home(req):
    return render(req,'admin_templates/home.html')

class CategoriesListView(LoginRequiredMixin,ListView):
    model = Categories
    template_name = "admin_templates/category_list.html"
    # The below are for the parent class LoginRequiredMixin.
    # This LoginRequiredMixin is a parent class for the django to overcome
    # the problem fo the login_required decorator with the models as it won't
    # work for the models. So inheriting this LoginRequiredMixin class
    # forces the request to get redirect to the login_url specified
    # for login.
    login_url = '/admin/'
    redirect_field_name = 'redirect_to'

class CategoriesCreateView(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    model = Categories
    success_message = "Category sucessfully added"
    fields = ('id','title','url_slug','thumbnail','description','is_active')
    # Mentioning here the fields is preferable as the jinja template follow the order
    # we mention here what ever the order it is in the models class,
    # If we mention '__all__' it will follow the order of the items or elements
    # in the order it was coded in the models class.
    template_name = 'admin_templates/category_create.html'
    # The below are for the parent class LoginRequiredMixin.
    # This LoginRequiredMixin is a parent class for the django to overcome
    # the problem fo the login_required decorator with the models as it won't
    # work for the models. So inheriting this LoginRequiredMixin class
    # forces the request to get redirect to the login_url specified
    # for login.
    login_url = '/admin/'
    redirect_field_name = 'redirect_to'
    
class CategoriesUpdateView(LoginRequiredMixin,SuccessMessageMixin,UpdateView):
    model = Categories
    success_message = "Category sucessfully updated"
    fields = ('id','title','url_slug','thumbnail','description','is_active')
    # Mentioning here the fields is preferable as the jinja template follow the order
    # we mention here what ever the order it is in the models class,
    # If we mention '__all__' it will follow the order of the items or elements
    # in the order it was coded in the models class.
    template_name = 'admin_templates/category_update.html'
    # The below are for the parent class LoginRequiredMixin.
    # This LoginRequiredMixin is a parent class for the django to overcome
    # the problem fo the login_required decorator with the models as it won't
    # work for the models. So inheriting this LoginRequiredMixin class
    # forces the request to get redirect to the login_url specified
    # for login.
    login_url = '/admin/'
    redirect_field_name = 'redirect_to'

class SubCategoriesListView(LoginRequiredMixin,ListView):
    model = SubCategories
    template_name = "admin_templates/sub_category_list.html"
    # The below are for the parent class LoginRequiredMixin.
    # This LoginRequiredMixin is a parent class for the django to overcome
    # the problem fo the login_required decorator with the models as it won't
    # work for the models. So inheriting this LoginRequiredMixin class
    # forces the request to get redirect to the login_url specified
    # for login.
    login_url = '/admin/'
    redirect_field_name = 'redirect_to'

class SubCategoriesCreateView(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    model = SubCategories
    success_message = "Sub Category sucessfully added"
    fields = ('category_id','title','url_slug','thumbnail','description','is_active')
    # fields = '__all__'
    # Mentioning here the fields is preferable as the jinja template follow the order
    # we mention here what ever the order it is in the models class,
    # If we mention '__all__' it will follow the order of the items or elements
    # in the order it was coded in the models class.
    template_name = 'admin_templates/sub_category_create.html'
    # The below are for the parent class LoginRequiredMixin.
    # This LoginRequiredMixin is a parent class for the django to overcome
    # the problem fo the login_required decorator with the models as it won't
    # work for the models. So inheriting this LoginRequiredMixin class
    # forces the request to get redirect to the login_url specified
    # for login.
    login_url = '/admin/'
    redirect_field_name = 'redirect_to'

class SubCategoriesUpdateView(LoginRequiredMixin,SuccessMessageMixin,UpdateView):
    model = SubCategories
    success_message = "Sub Category sucessfully updated"
    fields = ('category_id','title','url_slug','thumbnail','description','is_active')
    # fields = '__all__'
    # Mentioning here the fields is preferable as the jinja template follow the order
    # we mention here what ever the order it is in the models class,
    # If we mention '__all__' it will follow the order of the items or elements
    # in the order it was coded in the models class.
    template_name = 'admin_templates/sub_category_update.html'
    # The below are for the parent class LoginRequiredMixin.
    # This LoginRequiredMixin is a parent class for the django to overcome
    # the problem fo the login_required decorator with the models as it won't
    # work for the models. So inheriting this LoginRequiredMixin class
    # forces the request to get redirect to the login_url specified
    # for login.
    login_url = '/admin/'
    redirect_field_name = 'redirect_to'

class MerchantUserCreateView(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    # The below are for the parent class LoginRequiredMixin.
    # This LoginRequiredMixin is a parent class for the django to overcome
    # the problem fo the login_required decorator with the models as it won't
    # work for the models. So inheriting this LoginRequiredMixin class
    # forces the request to get redirect to the login_url specified
    # for login.
    login_url = '/admin/'
    redirect_field_name = 'redirect_to'

    template_name = "admin_templates/merchant_create.html"
    model = CustomUser
    fields = ("first_name","last_name","email","username","password")
    # fields = "__all__"

    def form_valid(self,form):
        
        # Saving CustomUser object for Merchant User
        user = form.save(commit=False)
        user.is_active=True
        user.user_type=3
        user.set_password(form.cleaned_data['password'])
        user.save()

        # Saving merchant user
        profile_pic = self.request.FILES["profile_pic"]
        fs=FileSystemStorage()
        filename=fs.save(profile_pic.name,profile_pic)
        profile_pic_url=fs.url(filename)

        user.merchantuser.profile_pic=profile_pic_url
        user.merchantuser.company_name=self.request.POST.get("company_name")
        user.merchantuser.gst_details=self.request.POST.get("gst_details")
        user.merchantuser.address=self.request.POST.get("address")
        is_added_by_admin = False
        if self.request.POST.get("is_added_by_admin")=="on":
            is_added_by_admin=True
        user.merchantuser.is_added_by_admin=is_added_by_admin
        user.save()
        messages.success(self.request,"Merchant User Created!")
        return HttpResponseRedirect(reverse("merchant_list_view"))
        
class MerchantUserListView(LoginRequiredMixin,ListView):
    model = MerchantUser
    template_name = "admin_templates/merchant_list.html"
    login_url = '/admin/'
    redirect_field_name = 'redirect_to'

class MerchantUserUpdateView(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    # The below are for the parent class LoginRequiredMixin.
    # This LoginRequiredMixin is a parent class for the django to overcome
    # the problem fo the login_required decorator with the models as it won't
    # work for the models. So inheriting this LoginRequiredMixin class
    # forces the request to get redirect to the login_url specified
    # for login.
    login_url = '/admin/'
    redirect_field_name = 'redirect_to'

    model = CustomUser
    success_message = "Merchant User sucessfully updated"
    fields = ("first_name","last_name","email","username","password")
    template_name = "admin_templates/merchant_update.html"
    # fields = "__all__"

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['merchantuser']=MerchantUser.objects.get(auth_user_id=self.get_object().pk)
        return context

    def form_valid(self,form):
        
        # Saving CustomUser object for Merchant User
        user = form.save(commit=False)
        user.is_active=True
        user.user_type=3
        user.set_password(form.cleaned_data['password'])
        user.save()

        # Saving merchant user
        profile_pic = self.request.FILES["profile_pic"]
        fs=FileSystemStorage()
        filename=fs.save(profile_pic.name,profile_pic)
        profile_pic_url=fs.url(filename)

        user.merchantuser.profile_pic=profile_pic_url
        user.merchantuser.company_name=self.request.POST.get("company_name")
        user.merchantuser.gst_details=self.request.POST.get("gst_details")
        user.merchantuser.address=self.request.POST.get("address")
        is_added_by_admin = False
        if self.request.POST.get("is_added_by_admin")=="on":
            is_added_by_admin=True
        user.merchantuser.is_added_by_admin=is_added_by_admin
        user.save()
        messages.success(self.request,"Merchant User Created!")
        return HttpResponseRedirect(reverse("merchant_list_view"))
