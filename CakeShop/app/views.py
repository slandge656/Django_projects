from django.shortcuts import render,redirect
from .models import Products,Category,CustomUser
from django.contrib.sessions.models import Session
from django.contrib import messages
from django.contrib.auth import login,logout
# Create your views here.
def User_Signup(request):
    if request.method=="POST":
        First_Name=request.POST['First_Name']
        Last_Name=request.POST['Last_Name']
        Mobile_No=request.POST['Mobile_No']
        Email=request.POST['Email']
        Password=request.POST['Password']
        RE_Password=request.POST['RE_Password']

        user_input={
            'First_Name':First_Name,
            'Last_Name':Last_Name,
            'Mobile_No':Mobile_No,
            'Email':Email,
            'Password':Password,
            'RE_Password':RE_Password
        }

        if len(Mobile_No) != 10:
            messages.warning(request, "Enter valid Mobile No.")
            return render(request,'app/signup.html',user_input)
        elif Password != RE_Password:
            messages.warning(request, "Enter correct Password.")
            return render(request,'app/signup.html',user_input)   
        else:
            data=CustomUser(
                First_Name=First_Name,
                Last_Name=Last_Name,
                Mobile_No=Mobile_No,
                Email=Email,
                Password=Password,
                RE_Password=RE_Password
            )
            data.register_user()
            messages.success(request,'Account Created...')
    return render(request,'app/signup.html')


def User_Login(request):
    if request.method=='POST':
        Mobile_No=request.POST['Mobile_No']
        print(Mobile_No)
        print(type(Mobile_No))
        user=CustomUser.objects.filter(Mobile_No = Mobile_No)

        
        if user:
            messages.success(request,'Success...')
            return redirect('home')
        else:
            messages.error(request,'Invalid Mobile No...')

    return render(request,'app/login.html')
def Home(request):
    if request.method =='POST':
        product_id=request.POST.get('product_id')
        cart=request.session.get('cart')
        if cart:
            quanitity=cart.get(product)
            cart[product]=quanitity+1
        else:
            cart={}
            cart[product]=1
        return redirect('home')

    else:
        categories=Category.get_all_categories()
        category_id=request.GET.get('category')
        print(category_id)
        cat_name_list=[]
        if category_id:
            print('yess')
            products=Products.get_products_by_category(category_id)
            if products:
                for product in products:
                    cat_name = product.category_name
                    cat_name=str(cat_name)
                    cat_name_list.append(cat_name)
                    break
            else:
                cat_name="No products found for this category."
                cat_name_list.append(cat_name) 
        
        else:
            products=Products.get_all_products()    
        cat_name_list=''.join(cat_name_list)
        
        context={
            'products':products,
            'categories':categories,
            'cat_name':cat_name_list
        }
        return render(request,'app/home.html',context)
    
