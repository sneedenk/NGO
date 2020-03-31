from .models import Donor
from .models import DonationDetails
from .models import Events
from django import forms
from users.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms.models import modelformset_factory
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.widgets import SelectDateWidget


class DonorForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = ('CMA_num', 'phone', 'address', 'city', 'state', 'zip_code', 'country', 'urbanization')


class DonationDetailsForm(forms.ModelForm):
    class Meta:
        model = DonationDetails
        fields = ('event', 'amount')


events = Events.objects.all().values_list('name', flat=True)
number_of_events = len(events)
EventFormSet = modelformset_factory(DonationDetails, fields=('amount',), extra=number_of_events, widgets={
    'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Donation Amount Here'})
    })


class EventForm(forms.ModelForm):
    date = forms.DateField(widget=SelectDateWidget())

    class Meta:
        model = Events
        fields = ('name', 'date')


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
