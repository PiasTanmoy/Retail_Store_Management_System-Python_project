from django.shortcuts import render
from .models import Product
from .models import Categorie
from .models import Stock

# Create your views here.

def showProducts(request):

    products = Product.objects.all()

    context = {
        'all_products': products
    }

    return render(request, 'Inventory/showproducts.html', context)

def showCategories(request):

    categories = Categorie.objects.all()

    context1 = {

        'all_categories': categories
    }
    return render(request, 'Inventory/Showcategories.html',context1)



