from django.shortcuts import render,redirect
from .models import Products,Category
from django.contrib.sessions.models import Session

# Create your views here.
def User_Signup(request):
    return render(request,'app/signup.html')

def User_Login(request):
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
    
