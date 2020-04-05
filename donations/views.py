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
<<<<<<< Updated upstream
=======
from django.views.generic.base import View
from django.forms import modelformset_factory
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
>>>>>>> Stashed changes
from donations.models import Donor
from donations.models import DonationDetails
from donations.models import Events
from donations.forms import DonorForm
from donations.forms import DonationDetailsForm
from donations.forms import EventForm
from donations.forms import CreateUserForm
from django.http import HttpResponseRedirect
from django.views.decorators.http import require_POST
from .models import Cart
from django.contrib.auth.decorators import login_required


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
<<<<<<< Updated upstream
=======

@login_required
def event_list(request):
    eventlist = Events.objects.all()
    # form = DonationDetailsForm
    context = {'events': eventlist}

    return render(request, 'donations/eventslist.html', context)


@require_POST
def cart_add(request, event_id):
    cart = Cart(request)
    #print(request.POST.get('event_id'))
    event = get_object_or_404(Events, id=event_id)
    amount = request.POST.get('amount')
    # amount = float(amount)
    #print(amount)
    try:
        amount = float(amount)
        cart.add(event = event, amount = amount)
    except:
        cart.add(event=event, amount=0)
    return redirect('donations:cart_details')


def cart_remove(request, event_id):
    cart = Cart(request)
    #print('*******')
    print(event_id)

    #event = get_object_or_404(Events, id=request.POST.get('event_id'))
    event = get_object_or_404(Events, id=event_id)
    print(event)
    cart.remove(event)
    return redirect('donations:cart_details')


def cart_details(request):
    cart = Cart(request)
    return render(request, 'donations/detail.html', {'cart': cart})


def add_to_cart(request):
    context = {'event_id': request.POST.get('event_id'), 'amount':  request.POST.get('amount')}
    return render(request, 'donations/cart.html', context)




>>>>>>> Stashed changes
