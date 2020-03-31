# from django.contrib.auth.models import User
from users.models import User
from django.urls import reverse
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.base import View
from django.forms import modelformset_factory
from django.shortcuts import render
from donations.models import Donor
from donations.models import DonationDetails
from donations.models import Events
from donations.forms import DonorForm
from donations.forms import DonationDetailsForm
from donations.forms import EventForm, EventFormSet
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

    def get(self, request, *args, **kwargs):
        user_ID = User.objects.values_list('id', flat=True).get(username__iexact=self.request.user)
        if Donor.objects.filter(user_id=user_ID).count() > 0:
            return HttpResponseRedirect(self.get_success_url())
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        user_ID = User.objects.values_list('id', flat=True).get(username__iexact=self.request.user)
        post = form.save(commit=False)
        post.user_id = user_ID
        post.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('donations:donation_details')


class DonationDetailsView(View):
    def post(self, request):
        event_formset = EventFormSet(request.POST)
        # post doesn't need to be authenticated because posts only originate internally, right? just gets?
        print("POST: ", request.POST)
        if event_formset.is_valid():
            events = Events.objects.all().values_list('id', flat=True)
            last_order = DonationDetails.objects.order_by('order').last()
            order = 1
            if last_order:
                order = last_order.order + 1
            for event_id, form in zip(events, event_formset):
                amount = form.cleaned_data.get('amount')
                if form.cleaned_data.get('amount'):
                    print("FORM: ", form)
                    print("FORM DICT: ", form.__dict__)
                    event = form.save(commit=False)
                    user = User.objects.get(username__iexact=self.request.user)
                    # donor_ID = Donor.objects.filter(user_id=user_ID).last()
                    # print("donor_ID: ", donor_ID, "type: ", type(donor_ID))
                    event.user = user
                    event.order = order
                    event.event = event_id
                    event.save()
            # event_formset.save()
            # context = {'event_formset': event_formset}
            return render(request, 'cart.html')  # using render
        context = {'event_formset': event_formset}
        return render(request, 'donation_details.html', context)

    def get(self, request):
        events = Events.objects.all().values_list('name', flat=True)
        event_formset = EventFormSet(queryset=DonationDetails.objects.none())
        for event, form in zip(events, event_formset):
            form.fields['amount'].label = event
        # print(event_formset)
        context = {'event_formset': event_formset}
        return render(request, 'donation_details.html', context)


# class DonationDetailsView(CreateView):
#     model = DonationDetails
#     template_name = 'donation_details.html'
#     form_class = DonationDetailsForm
#
#     def form_valid(self, form):
#         # get order number
#         # filter on "order", check len(queryset) if its 0, set order=0, otherwise order = last + 1
#         # apply order # to all rows saved from this transaction
#
#         print("USER ID: ", self.request.user)
#         donor_ID = Donor.objects.values_list('id', flat=True).filter(user=self.request.user).last()
#         #order_ID = DonationDetails.objects.values_list('order', flat=True).filter(donor_ID)
#         #print("ORDER: ", DonationDetails.objects.values_list('order', flat=True).filter(donor_ID))
#         queryset = DonationDetails.objects.values_list('order', flat=True)
#         print("QS LENGTH: ", len(queryset))
#         print(queryset)
#         # if len(queryset) == 0:
#         #     print("EMPTY QUERYSET")
#         #     order_ID = 1
#
#         print("RIGHT HERE", donor_ID)
#         post = form.save(commit=False)
#         post.donor_id = donor_ID
#         #post.order = order_ID
#         # print(post.user_id)
#         print(self.request.user)
#         post.save()
#         return HttpResponseRedirect(self.get_success_url())
#
#     def get_success_url(self):
#         return reverse('donations:cart')


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


class displayCart():
    pass
