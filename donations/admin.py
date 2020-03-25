from django.contrib import admin
from .models import Donor
from .models import DonationDetails
from .models import Events
# from django.contrib.auth.models import User

# Register your models here.
admin.site.register(Donor)
admin.site.register(DonationDetails)
admin.site.register(Events)
