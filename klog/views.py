from django.shortcuts import redirect, render, HttpResponse
from django.http import JsonResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http.response import HttpResponseRedirect
from klog import forms
from klog.forms import customerForm 
from klog.forms import categoryForm
from klog.models import customer
from klog.models import product
from klog.models import Categrory

# Create your views here.
def index(request):
    user=request.session.get('username')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            request.session['id'] = user.id
            request.session['username']=user.username

            
            return JsonResponse({'success': True},safe=False)
        else:
            
            return JsonResponse({'success': False},safe=False)
    elif(user):
        return redirect('/register')
    else:
        return render(request, "index.html",{'user':user})

   

def register(request):
    user=request.session.get('username')
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if (password1 == password2):
            if User.objects.filter(username=username):
                messages.info(request, "username already in use")
                return redirect('/')
            elif User.objects.filter(email=email):
                messages.info(request, "Email already in use")
                return redirect('/')
            else:
                users = User.objects.create_user(
                    first_name=first_name, last_name=last_name, username=username, email=email, password=password1)
                users.save()
                return redirect('/')
        else:
            messages.info(request, "Password not matching")
        return redirect('/') 
    elif(user):
        return redirect('/adminpanel')
    else:
        return render(request, "register.html",{'user':user})

 
   
def Logout(request):
    try:
        request.session.flush()
    except:
        pass    
    return redirect("/")    

def adminpanel(request):
    user=request.session.get('username')
    if(user):
        
        
        return render(request, "adminpanel.html", {'user': user})
    else:
        user=request.session.get('username')

def forms(request):
    return render(request, "forms.html")  





 
  

def addnew(request):
    customerForm = forms.customerForm()
    if request.method=='POST':
        customerForm = forms.customerForm(request.POST)
        if customerForm.is_valid():
            data = customerForm.save() ;
            return HttpResponseRedirect('/detail')

    context = {'customerForm' : customerForm}
    return render(request, 'addnew.html',context)

def detail(request):
    user=request.session.get('username') 
    if(user):
        
        datas = customer.objects.all() 
        
        return render(request, "detail.html", {'datas': datas,'user': user})
    else:
        user=request.session.get('username') 


def detailupdate(request, id):  
    data = customer.objects.get(id=id)
    form = customerForm(initial={'name': data.name, 'contact': data.contact, 'email': data.email})
    if request.method == "POST":  
        form = customerForm(request.POST, instance=data)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('detail')  
            except Exception as e: 
                pass    
    return render(request,'detailupdate.html',{'form':form})  

def detaildelete(request, id):
    book = customer.objects.get(id=id)
    try:
        book.delete()
    except:
        pass
    return redirect('detail')

def productdetail(request):
    user=request.session.get('username') 
    if(user):
        
        prod = product.objects.all() 
        
        return render(request, "productdetail.html", {'prod': prod})
    else:
        user=request.session.get('username') 


def addproduct(request):
    if request.method == "POST":
        prod = product()
        prod.product_name = request.POST.get('product_name')
        prod.disc = request.POST.get('disc')
        prod.price = request.POST.get('price')
        prod.weight = request.POST.get('weight')
        prod.category = request.POST.get('category')

        if len(request.FILES) != 0:
            prod.image = request.FILES['image']

        prod.save()
        messages.success(request, "Product Added Successfully")
        return redirect('/productdetail')
    return render(request, 'addproduct.html')

def productcategory(request):
     products = Categrory.objects.all()
     
     return render(request,"productcategory.html", {'products':products})

def categoryupdate(request, id):  
    dat = Categrory.objects.get(id=id)
    fore = categoryForm(initial={'cname': dat.cname})
    if request.method == "POST":  
        fore = customerForm(request.POST, instance=dat)  
        if fore.is_valid():  
            try:  
                fore.save() 
                model = form.instance
                return redirect('productcategory')  
            except Exception as e: 
                pass    
    return render(request,"categoryupdate.html",{'fore':fore})  
     


