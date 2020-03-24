from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from donations.models import Donor
from donations.models import DonationDetails
from donations.models import DonationType
from donations.models import Events
from donations.forms import DonorForm
from donations.forms import DonationDetailsForm
from donations.forms import EventForm
from donations.forms import CreateUserForm
from django.http import HttpResponseRedirect


# Generic class based views here.
class DonationTypeView(ListView):
    model = DonationType
    template_name = 'make_donation.html'


class DonorInfoView(CreateView):
    model = Donor
    template_name = 'donor_info.html'
    form_class = DonorForm

    def get_success_url(self):
        return reverse('donations:donation_info', args=[self.object.id])


class DonationDetailsView(CreateView):
    model = DonationDetails
    template_name = 'donation_details.html'
    form_class = DonationDetailsForm

    def get_success_url(self):
        return reverse('donations:cart')


class CreateEventView(CreateView):
    model = Events
    template_name = 'create_event.html'
    form_class = EventForm


# class ProductListGenericView(ListView):
#     model = Product
#     template_name = 'make_donation.html'
#
#
# class ProductDetailsGenericView(DetailView):
#     model = Product
#     template_name = 'product_details.html'
#
#
# class NewProductGenericView(LoginRequiredMixin, CreateView):
#     model = Product
#     template_name = 'new_product.html'
#     # fields = ('name', 'price', 'image')
#     form_class = ProductForm
#
#     def get_success_url(self):
#         return reverse('donations:product_details', args=[self.object.id])
#
#
# class UpdateProductGenericView(LoginRequiredMixin, UpdateView):
#     model = Product
#     template_name = 'update_product.html'
#     #fields = ('name', 'price')
#     form_class = ProductForm
#
#     # def get_object(self):  # and you have to override a get_object method
#     #     return get_object_or_404(Product, image=self.request.GET.get('pk'))
#
#     def get_success_url(self):
#         return reverse('donations:product_details', args=[self.object.id])
#
#
# class DeleteProductGenericView(LoginRequiredMixin, DeleteView):
#     model = Product
#     success_url = reverse_lazy('product_list')
#
#     def get(self, request, pk):
#         # if request.user.is_authenticated:
#         product = Product.objects.get(pk=pk)
#         product.delete()
#         # product.save() # I guess this isn't necessary as delete already saves to the DB
#         return HttpResponseRedirect('/')


class CreateUserView(CreateView):
    model = User
    form_class = CreateUserForm
    template_name = 'new_user.html'
    # fields = ('username', 'password', 'first_name', 'last_name', 'email')

    def get_success_url(self):
        return reverse('product_list')


# Class based views here.
# class ProductListView(View):
#     def get(self, request):
#         products = Product.objects.all()
#         return render(request, 'make_donation.html', {'products': products})
#
#
# class ProductDetailsView(View):
#     def get(self, request, pk):
#         product = Product.objects.get(pk=pk)
#         return render(request, 'product_details.html', {'product': product})
#
#
# # converted to LoginRequiredMixin rather than through if-else block
# class NewProductView(LoginRequiredMixin, View):
#     def post(self, request):
#         # post doesn't need to be authenticated because posts only originate internally, right? just gets?
#         form = ProductForm(request.POST)
#         if form.is_valid():
#             product = form.save()
#             return render(request, 'product_details.html', {'product': product})  # using render
#         return render(request, 'new_product.html')
#
#     def get(self, request):
#         # if request.user.is_authenticated:
#         product_form = ProductForm()
#         return render(request, 'new_product.html', {'product_form': product_form})
#         # else:
#         #     return HttpResponseRedirect('/accounts/login/?next=/')
#
#
# class UpdateProductView(View):
#     def get(self, request, pk):
#         product = Product.objects.get(pk=pk)
#         product_form = ProductForm(instance=product)
#         return render(request, 'update_product.html', {'product_form': product_form})
#
#     def post(self, request, pk):
#         product_form = ProductForm(request.POST)
#         if product_form.is_valid():
#             Product.objects.filter(id=pk).update(name=request.POST['name'], price=request.POST['price'])
#             product = Product.objects.get(pk=pk)
#             return render(request, 'product_details.html', {'product': product})  # using render
#         return render(request, 'update_product.html')
#
#
# # converted to LoginRequiredMixin rather than through if-else block
# class DeleteProductView(LoginRequiredMixin, View):
#     def get(self, request, pk):
#         # if request.user.is_authenticated:
#         product = Product.objects.get(pk=pk)
#         product.delete()
#         # product.save() # I guess this isn't necessary as delete already saves to the DB
#         return HttpResponseRedirect('/')
#         # else:
#         #     return HttpResponseRedirect('/accounts/login/?next=/')
#
#
# # Function based views here.
# def product_list(request):
#     products = Product.objects.all()
#     print(products)
#     # see settings.py
#     # 'DIRS': [r'C:\Users\UCI\Documents\GitHub\SummitWorks\DjangoWork\ngo\donations\templates\donations'],
#     # should be able to access make_donation.html without additional directories here
#     return render(request, 'make_donation.html', {'products': products})
#
#
# def product_details(request, pk):
#     product = Product.objects.get(pk=pk)
#     return render(request, 'product_details.html', {'product': product})
#
#
# @login_required
# def new_product(request):
#     if request.method == "POST":
#         form = ProductForm(request.POST)
#         if form.is_valid():
#             product = form.save()
#             return render(request, 'product_details.html', {'product': product}) # using render
#             # note: redirect with render() doesn't change the URL, still /new_product/
#             # using HttpResponseRedirect below, the URL updates to /pk/
#             # return HttpResponseRedirect('/%i' % product.pk) # view the new product's details with HttpResponseRedirect
#             # return HttpResponseRedirect('/') # back to root
#     else:
#         product_form = ProductForm()
#         return render(request, 'new_product.html', {'product_form': product_form})
#     return render(request, 'new_product.html')
#
#
# @login_required
# def update_product(request, pk):
#     if request.method == "POST":
#         product_form = ProductForm(request.POST)
#         if product_form.is_valid():
#             Product.objects.filter(id=pk).update(name=request.POST['name'], price=request.POST['price'])
#             product = Product.objects.get(pk=pk)
#             return render(request, 'product_details.html', {'product': product}) # using render
#             # note: redirect with render() doesn't change the URL, still /new_product/
#             # using HttpResponseRedirect below, the URL updates to /pk/
#             # return HttpResponseRedirect('/%i' % product.pk) # view the new product's details with HttpResponseRedirect
#             # return HttpResponseRedirect('/') # back to root
#     else:
#         product = Product.objects.get(pk=pk)
#         product_form = ProductForm(instance=product)
#         return render(request, 'update_product.html', {'product_form': product_form})
#     return render(request, 'update_product.html')
#
#
# @login_required
# def delete_product(request, pk):
#     product = Product.objects.get(pk=pk)
#     product.delete()
#     # product.save() # I guess this isn't necessary as delete already saves to the DB
#     return HttpResponseRedirect('/')
#
#
# # need to fix so users are automatically logged in up successful sign up
# # skipped porting to class based view, just class based generic view is implemented
# def create_user(request):
#     if request.method == "POST":
#         new_user = CreateUserForm(request.POST)
#         if new_user.is_valid():
#             username = new_user['username'].value()
#             first_name = new_user['first_name'].value()
#             last_name = new_user['last_name'].value()
#             email = new_user['email'].value()
#             password = new_user['password'].value()
#             user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
#             # user.save()
#             return HttpResponseRedirect('/')
#     else:
#         new_user_form = CreateUserForm()
#         return render(request, 'new_user.html', {'new_user_form': new_user_form})
#     return render(request, 'new_user.html', {'new_user': new_user})
#
#
#
# def successpage(request):
#     products = Product.objects.all()
#     return render(request, 'make_donation.html', {'products': products})


