from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth.models import User
from users.models import User
from django.contrib.auth import authenticate, login
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from donations.models import Donor
from donations.models import DonationDetails
from donations.models import Events
from donations.forms import DonorForm
from donations.forms import DonationDetailsForm
from donations.forms import EventForm
from donations.forms import CreateUserForm
from django.http import HttpResponseRedirect


# Generic class based views here.
class EventListView(ListView):
    model = Events
    template_name = 'events.html'


class EventDetailsView(DetailView):
    model = Events
    template_name = 'event_details.html'


class DonorInfoView(CreateView):
    model = Donor
    template_name = 'donor_info.html'
    form_class = DonorForm

    def form_valid(self, form):
        print("USER ID: ", self.request.user)
        user_ID = User.objects.values_list('id', flat=True).get(username__iexact=self.request.user)
        print("RIGHT HERE", user_ID)
        post = form.save(commit=False)
        post.user_id = user_ID
        # print(post.user_id)
        print(self.request.user)
        post.save()
        return HttpResponseRedirect(self.get_success_url())

    # def post(self, request, *args, **kwargs):
    #     form = self.get_form()
    #     if form.is_valid():
    #         post = form.save(commit=False)
    #         # post.author = request.user
    #         post.user_id = request.user.id
    #         post.save()
    #         return self.form_valid(form)
    #     else:
    #         return self.form_invalid(form)


    def get_success_url(self):
        return reverse('donations:donation_details')


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

    def get_success_url(self):
        return reverse('donations:event_details', args=[self.object.id])


class CreateUserView(CreateView):
    model = User
    form_class = CreateUserForm
    template_name = 'new_user.html'
    # fields = ('username', 'password', 'first_name', 'last_name', 'email')

    def get_success_url(self):
        return reverse('list_events')
