from django.shortcuts import render, get_object_or_404, redirect
from productapp.models import Product
from productapp.forms import ProductForm
from django.http import HttpResponseRedirect
from datetime import datetime


# Create your views here.
def product_list(request):
    products = Product.objects.all()
    print(products)
    # see settings.py
    # 'DIRS': [r'C:\Users\UCI\Documents\GitHub\SummitWorks\DjangoWork\PracticeWork\inventory_app\productapp\templates\productapp'],
    # should be able to access make_donation.html without additional directories here
    return render(request, 'make_donation.html', {'products': products})


def product_details(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'product_details.html', {'product': product})


def new_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save()
            return render(request, 'product_details.html', {'product': product}) # using render
            # note: redirect with render() doesn't change the URL, still /new_product/
            # using HttpResponseRedirect below, the URL updates to /pk/
            # return HttpResponseRedirect('/%i' % product.pk) # view the new product's details with HttpResponseRedirect
            # return HttpResponseRedirect('/') # back to root
    else:
        form = ProductForm()
        return render(request, 'new_product.html', {'form': form})
    return render(request, 'new_product.html')


def successpage(request):
    products = Product.objects.all()
    return render(request, 'make_donation.html', {'products': products})


