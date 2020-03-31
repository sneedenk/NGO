from django.db import models
from users.models import User


class Donor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    CMA_num = models.IntegerField(null=False, blank=False)
    phone = models.CharField(max_length=40, null=False, blank=False)
    address = models.CharField(max_length=100, null=False, blank=False)
    city = models.CharField(max_length=40, null=False, blank=False)
    state = models.CharField(max_length=40, null=False, blank=False)
    zip_code = models.CharField(max_length=40, null=False, blank=False)
    country = models.CharField(max_length=40, null=False, blank=False)
    urbanization = models.CharField(max_length=40, null=True, blank=True)
    date = models.DateField(auto_now=True)


class DonationDetails(models.Model):
    order = models.IntegerField(default=1, null=False)  # user doesn't fill this in
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.CharField(max_length=40, null=False, blank=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)


class Events(models.Model):
    name = models.CharField(max_length=40, null=False, blank=False)
    date = models.DateField(null=False, blank=False)
