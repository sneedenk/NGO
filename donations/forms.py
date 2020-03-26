from .models import Donor
from .models import DonationDetails
from .models import Events
from django import forms
from users.models import User
from django.contrib.auth.forms import UserCreationForm


class DonorForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = ('CMA_num', 'phone', 'address', 'city', 'state', 'zip_code', 'country', 'urbanization')


class DonationDetailsForm(forms.ModelForm):
    class Meta:
        model = DonationDetails
        fields = ('event', 'amount')


class EventForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = ('name', 'date')


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
