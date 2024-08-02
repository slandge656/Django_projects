from django.shortcuts import render,redirect
from .models import Products,Category,CustomUser
from django.contrib.sessions.models import Session
from django.contrib import messages
from django.contrib.auth import login,logout
from django.utils import timezone
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
        user=CustomUser.objects.get(Mobile_No = Mobile_No)

        
        if user:
            user.last_login_time = timezone.now()
            user.save()
            request.session["user_id"] = user.id
            print(request.session["user_id"],'user_id')
            request.session["user_email"] = user.Email
            messages.success(request,'Success...')
            return redirect('home')
        else:
            messages.error(request,'Invalid Mobile No...')

    return render(request,'app/login.html')


def User_Logout(request):
    request.session.clear()
    return redirect('login')
def Home(request):
    if 'cart' not in request.session:
        request.session['cart'] = {}
        
    if request.method =='POST':
        product_id=request.POST.get('product_id')
        remove_item=request.POST.get('remove_item')
        print(product_id)
        cart=request.session.get('cart',{})
        if cart:
            quanitity=cart.get(product_id)
            if quanitity:
                if remove_item:  
                    if quanitity <=1:
                        cart.pop(product_id)
                    else:
                        cart[product_id]=quanitity-1
                else:
                    cart[product_id]=quanitity+1   
            else:
                cart[product_id]=1    
        else:
            cart[product_id]=1
        request.session['cart']=cart
        print(request.session['cart'])    
        return redirect('home')

    else:
        print(request.session.get('cart'),'hiiiii')
        latest_user = CustomUser.objects.order_by('-last_login_time').first()
        # print(latest_user)
        categories=Category.get_all_categories()
        category_id=request.GET.get('category')
        # print(category_id)
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
        
        print(request.session.get('user_email'))
        context={
            'products':products,
            'categories':categories,
            'cat_name':cat_name_list,
            'latest_user':latest_user
        }
        return render(request,'app/home.html',context)
    
