from django.shortcuts import render
from .models import Products,Category
# Create your views here.
def Home(request):
    products=Products.get_all_products()
    categories=Category.get_all_categories()

    context={
        'products':products,
        'categories':categories
    }
    return render(request,'app/home.html',context)