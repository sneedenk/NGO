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

    def get_success_url(self):
        return reverse('donations:donation_details', args=[self.object.id])


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


class CreateUserView(CreateView):
    model = User
    form_class = CreateUserForm
    template_name = 'new_user.html'
    # fields = ('username', 'password', 'first_name', 'last_name', 'email')

    def get_success_url(self):
        return reverse('list_events')
