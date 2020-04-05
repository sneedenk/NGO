from django.db import models
<<<<<<< Updated upstream
from django.utils import timezone
from django.contrib.auth.models import User
from django.forms.widgets import SelectDateWidget


# # Create your models here.
# # class Product(models.Model):
# #     name = models.CharField(max_length=20)
# #     price = models.IntegerField()
# #     image = models.ImageField(upload_to='images', default=None, null=True, blank=True)
# #
# #     # you can call save() from Model class to save Product
# #
# #     def __str__(self):
# #         return self.name
=======
from users.models import User
from decimal import Decimal
from django.conf import settings
>>>>>>> Stashed changes


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
    class Meta:
        constraints = [models.UniqueConstraint(fields=['donor', 'donation_type'], name='unique_donation')]

    donor = models.ForeignKey('Donor', on_delete=models.CASCADE)
    donation_type = models.CharField(max_length=40, null=False, blank=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)


class Events(models.Model):
    name = models.CharField(max_length=40, null=False, blank=False)
    date = models.DateField(null=False, blank=False)


class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def __iter__(self):

        event_ids = self.cart.keys()
        events = Events.objects.filter(id__in=event_ids)
        for event in events:
            self.cart[str(event.id)]['event'] = event

        for value in self.cart.values():
            value['amount'] = Decimal(value['amount'])
            yield value

    def add(self, event, amount):
        event_id = str(event.id)
        if event_id not in self.cart:
            self.cart[event_id]={'amount': amount}
        self.save()

    def remove(self, event):
        event_id = str(event.id)
        if event_id in self.cart:
            del self.cart[event_id]
            self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True








