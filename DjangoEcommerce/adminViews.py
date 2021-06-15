from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,View,DeleteView
from django.contrib.messages.views import SuccessMessageMixin,messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.storage import FileSystemStorage
from django.urls import reverse
from django.http import HttpResponseRedirect,HttpResponse
from django.db.models import Q

from DjangoEcommerceApp.models import Categories,SubCategories,MerchantUser,CustomUser,Products,ProductMedia,ProductDetails,ProductAbout,ProductTags,ProductTransaction

@login_required(login_url="/admin/")
def admin_home(req):
    print("The user is:",req.user.username)
    return render(req,'admin_templates/home.html')

class CategoriesListView(LoginRequiredMixin,ListView):
    model = Categories
    template_name = "admin_templates/category_list.html"
    paginate_by = 4
    sorting_fields = ('id','title','description')


    def get_queryset(self):
        filter_val = self.request.GET.get("filter","")
        order_by = self.request.GET.get("orderby","id")
        if filter_val!="":
            cat = self.model.objects.filter(Q(title__contains=filter_val) | Q(description__contains=filter_val)).order_by(order_by)
        elif order_by!="":
            cat = self.model.objects.all().order_by(order_by)
        else:
            cat = self.model.objects.all()
        return cat
    
    def get_context_data(self,**kwargs):
        context = super(self.__class__,self).get_context_data(**kwargs)
        context["filter"]=self.request.GET.get('filter','')
        context["orderby"]=self.request.GET.get('orderby','')
        context["all_table_fields"]=self.model._meta.get_fields()
        context['sorting_fields']=self.sorting_fields
        return context

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
    paginate_by = 4
    sorting_fields = ("id",'title','description') # These fields are for sorting the objects in the template handled by this view.

    def get_queryset(self):
        filter_val = self.request.GET.get("filter","")
        order_by = self.request.GET.get("orderby","id")
        if filter_val!="":
            cat = self.model.objects.filter(Q(title__contains=filter_val) | Q(description__contains=filter_val)).order_by(order_by)
        elif order_by!="":
            cat = self.model.objects.all().order_by(order_by)
        else:
            cat = self.model.objects.all()
        return cat
    
    def get_context_data(self,**kwargs):
        context = super(self.__class__,self).get_context_data(**kwargs)
        context["filter"]=self.request.GET.get('filter','')
        context["orderby"]=self.request.GET.get('orderby','')
        context["all_table_fields"]=self.model._meta.get_fields()
        # The below one is to add the fields for sorting provided in the class to the template context so as to make it available for the use in template .
        context['sorting_fields'] = self.sorting_fields
        return context
    
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
    paginate_by = 4

    def get_queryset(self):
        filter_val = self.request.GET.get("filter","")
        order_by = self.request.GET.get("orderby","id")
        if filter_val!="":
            cat = self.model.objects.filter(Q(title__contains=filter_val) | Q(description__contains=filter_val)).order_by(order_by)
        elif order_by!="":
            cat = self.model.objects.all().order_by(order_by)
        else:
            cat = self.model.objects.all()
        return cat
    
    def get_context_data(self,**kwargs):
        context = super(self.__class__,self).get_context_data(**kwargs)
        context["filter"]=self.request.GET.get('filter','')
        context["orderby"]=self.request.GET.get('orderby','')
        context["all_table_fields"]=self.model._meta.get_fields()
        return context

    login_url = '/admin/'
    redirect_field_name = 'redirect_to'

class MerchantUserUpdateView(LoginRequiredMixin,SuccessMessageMixin,UpdateView):
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
        user.set_password(form.cleaned_data['password'])
        user.save()

        # Saving merchant user
        merchant_user = MerchantUser.objects.get(auth_user_id=user.id)
        if self.request.FILES.get("profile_pic",False):
            profile_pic = self.request.FILES["profile_pic"]
            print("\nProfile pic is:",profile_pic,end="\n\n")
            fs=FileSystemStorage()
            filename=fs.save(profile_pic.name,profile_pic)
            profile_pic_url=fs.url(filename)
            print("\nProfile pic is:",filename,"\n\n",profile_pic.name,end="\n\n")

            merchant_user.profile_pic=profile_pic_url
        merchant_user.company_name=self.request.POST.get("company_name")
        merchant_user.gst_details=self.request.POST.get("gst_details")
        merchant_user.address=self.request.POST.get("address")
        is_added_by_admin = False
        if self.request.POST.get("is_added_by_admin")=="on":
            is_added_by_admin=True
        merchant_user.is_added_by_admin=is_added_by_admin
        merchant_user.save()
        messages.success(self.request,"Merchant User Updated!")
        return HttpResponseRedirect(reverse("merchant_list_view"))

class ProductCreateView(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    model = Products
    media_types = {value:i for i,value in ProductMedia.media_type_choices}
    # print("Media types in ProductCreateView are:",media_types)
    success_message = "Product sucessfully added"
    fields = ('id','product_name',"brand",'url_slug',"subcategories_id","product_max_price","product_discount_price","product_description","product_long_description",'added_by_merchant','in_stock_total')
    # fields = '__all__'
    template_name = 'admin_templates/product_create.html'
    login_url = '/admin/'
    redirect_field_name = 'redirect_to'

    def get_context_data(self,**kwargs):
        print("Ruquest reported at get_context_data from adminViews.ProductCreateView")
        context = super().get_context_data(**kwargs)
        categories = Categories.objects.filter(is_active=True)
        categories_list = [{"category":i,"sub_category":SubCategories.objects.filter(is_active=1,category_id=i.id)} for i in categories]
        merchant_users = MerchantUser.objects.filter(auth_user_id__is_active=True)
        context['categories'] = categories_list
        context['merchant_users'] = merchant_users
        return context
    
    def form_valid(self,form):
        print("Request reported at form_valid in adminViews.ProductCreateView")
        products = form.save(commit=False)
        products.is_active=True
        products.save()

        if self.request.FILES.getlist("media_content[]",False):
            media_content = self.request.FILES.getlist("media_content[]")
            print("\nLength of the media content is:",len(media_content))
            print("\nMedia content is:",media_content)
            media_content_uploaded = []
            media_type_uploaded = []

            # Saving media
            for media_obj in media_content:
                fs=FileSystemStorage()
                filename=fs.save(name=media_obj.name,content=media_obj)
                media_content_uploaded.append(media_obj)
                media_type_uploaded.append(self.media_types[media_obj.content_type.split('/')[0].capitalize()])
                print("Media type uploaded file is:",media_type_uploaded[-1])
                productmedia = ProductMedia(product_id=products,media_type=media_type_uploaded[-1],media_content=fs.url(filename))
                productmedia.save()
            print("\nMedia content of uploads are:",media_content_uploaded)
            print("\nMedia type of uploads are:",media_type_uploaded)
        
        product_details_title = self.request.POST.getlist("title_title[]")
        product_details_details = self.request.POST.getlist("title_details[]")
        print("Product details title:",product_details_title)
        print("Product details details:",product_details_details)
        if len(product_details_title)==len(product_details_details):
            for i in range(len(product_details_title)):
                product_details = ProductDetails(title = product_details_title[i],product_id = products,title_details = product_details_details[i])
                product_details.save()
        
        product_about = self.request.POST.getlist("about_title[]")
        for i in product_about:
            product_about = ProductAbout(title=i,product_id=products)
            product_about.save()

        product_tags = self.request.POST.get("product_tags[]").split(',')
        print("Product tags are:",product_tags)
        for i in product_tags:
            producttags = ProductTags(title=i,product_id=products)
            producttags.save()
    
        product_transaction = ProductTransaction(product_id=products,transaction_type=1,transaction_product_count=self.request.POST.get("in_stock_total"),transaction_description="Initially item added in stocks")
        product_transaction.save()

        messages.success(self.request,"Product Created!")
        return HttpResponseRedirect(reverse("product_list_view"))

class ProductListView(LoginRequiredMixin,ListView):
    model = Products
    template_name = "admin_templates/product_list.html"
    paginate_by = 4
    sorting_fields = ("id",'brand','product_max_price') # These fields are for sorting the objects in the template handled by this view.

    def get_queryset(self):
        filter_val = self.request.GET.get("filter","")
        order_by = self.request.GET.get("orderby","id")
        if filter_val!="":
            products = self.model.objects.filter(Q(product_name__contains=filter_val) | Q(product_description__contains=filter_val)).order_by(order_by)
        elif order_by!="":
            products = self.model.objects.all().order_by(order_by)
        else:
            products = self.model.objects.all()
        
        product_list = []
        for i in products:
            product_media = ProductMedia.objects.filter(product_id=i.id,is_active=1,media_type=1).first() # This is to show the images in the product list view.
            product_tags = ProductTags.objects.filter(product_id=i.id)
            print("\n\nFrom get_queryset method of ProductListView. Product tags are:",product_tags,end="\n\n")
            product_list.append({"product":i,"media":product_media,"tags":product_tags})
        # return products
        return product_list
    
    def get_context_data(self,**kwargs):
        context = super(self.__class__,self).get_context_data(**kwargs)
        context["filter"]=self.request.GET.get('filter','')
        context["orderby"]=self.request.GET.get('orderby','')
        context["all_table_fields"]=self.model._meta.get_fields()
        # The below one is to add the fields for sorting provided in the class to the template context so as to make it available for the use in template .
        context['sorting_fields'] = self.sorting_fields
        return context
    
    # The below are for the parent class LoginRequiredMixin.
    # This LoginRequiredMixin is a parent class for the django to overcome
    # the problem fo the login_required decorator with the models as it won't
    # work for the models. So inheriting this LoginRequiredMixin class
    # forces the request to get redirect to the login_url specified
    # for login.
    login_url = '/admin/'
    redirect_field_name = 'redirect_to'

class ProductUpdateView(LoginRequiredMixin,SuccessMessageMixin,UpdateView):
    model = Products
    media_types = {value:i for i,value in ProductMedia.media_type_choices}
    fields = ('id','product_name',"brand",'url_slug',"subcategories_id","product_max_price","product_discount_price","product_description","product_long_description",'added_by_merchant','in_stock_total')
    # fields = '__all__'
    # Mentioning here the fields is preferable as the jinja template follow the order
    # we mention here what ever the order it is in the models class,
    # If we mention '__all__' it will follow the order of the items or elements
    # in the order it was coded in the models class.
    template_name = 'admin_templates/product_update.html'
    # The below are for the parent class LoginRequiredMixin.
    # This LoginRequiredMixin is a parent class for the django to overcome
    # the problem fo the login_required decorator with the models as it won't
    # work for the models. So inheriting this LoginRequiredMixin class
    # forces the request to get redirect to the login_url specified
    # for login.
    login_url = '/admin/'
    redirect_field_name = 'redirect_to'

    def get_context_data(self,**kwargs):
        context = super(self.__class__,self).get_context_data(**kwargs)
        context['merchant_users'] = MerchantUser.objects.filter(is_active=1)
        # context['subcategories'] = SubCategories.objects.filter(is_active=1,category_id = SubCategories)
        context['categories'] = Categories.objects.filter(is_active=1)
        context['categories_list'] = [{"category":i,"subcategories":SubCategories.objects.filter(is_active=1,category_id=i.id)} for i in context['categories']]
        # print("\nProduct id is:",self.get_object().pk)
        context['product_details_list'] = ProductDetails.objects.filter(product_id=self.get_object().pk)
        # print("Product details are:",context['product_details_list'])
        context['product_about_list'] = ProductAbout.objects.filter(product_id=self.get_object().pk)
        context['product_tags_list'] = ProductTags.objects.filter(product_id=self.get_object().pk)
        context['product_media_list'] = ProductMedia.objects.filter(product_id=self.get_object().pk)
        # print("Categories and category lists are:",context['categories_list'])
        return context
    
    def form_valid(self,form):
        print("Request reported at form_valid in adminViews.ProductCreateView")
        products = form.save(commit=False)
        products.is_active=True
        products.save()

        if self.request.FILES.getlist("media_content[]",False):
            media_content = self.request.FILES.getlist("media_content[]")
            print("\nLength of the media content is:",len(media_content))
            print("\nMedia content is:",media_content)
            media_content_uploaded = []
            media_type_uploaded = []

            # Saving media
            for media_obj in media_content:
                fs=FileSystemStorage()
                filename=fs.save(name=media_obj.name,content=media_obj)
                media_content_uploaded.append(media_obj)
                media_type_uploaded.append(self.media_types[media_obj.content_type.split('/')[0].capitalize()])
                print("Media type uploaded file is:",media_type_uploaded[-1])
                productmedia = ProductMedia(product_id=products,media_type=media_type_uploaded[-1],media_content=fs.url(filename))
                productmedia.save()
            print("\nMedia content of uploads are:",media_content_uploaded)
            print("\nMedia type of uploads are:",media_type_uploaded)
        
        product_details_title = self.request.POST.getlist("title_title[]")
        product_details_details = self.request.POST.getlist("title_details[]")
        print("Product details title:",product_details_title)
        print("Product details details:",product_details_details)
        if len(product_details_title)==len(product_details_details):
            for i in range(len(product_details_title)):
                product_details = ProductDetails(title = product_details_title[i],product_id = products,title_details = product_details_details[i])
                product_details.save()
        
        product_about = self.request.POST.getlist("about_title[]")
        for i in product_about:
            product_about = ProductAbout(title=i,product_id=products)
            product_about.save()
        
        product_tags = self.request.POST.get("product_tags[]").split(',')
        print("Product tags are:",product_tags)
        for i in product_tags:
            producttags = ProductTags(title=i,product_id=products)
            producttags.save()
    
        product_transaction = ProductTransaction(product_id=products,transaction_type=1,transaction_product_count=self.request.POST.get("in_stock_total"),transaction_description="Updated item count in stocks")
        product_transaction.save()
        
        messages.success(self.request,f"Product Updated!")
        return HttpResponseRedirect(reverse("product_list_view"))