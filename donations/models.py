from django.db import models
from users.models import User
from decimal import Decimal
from django.conf import settings


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


class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}

        self.cart = cart

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def __iter__(self):
        donations_ids = self.cart.keys()
        donations = DonationDetails.objects.filter(id__in=donations_ids)
        for donation in donations:
            self.cart[str(donation.id)]['donation'] = donation

        for item in self.cart.values():
            item['amount'] = Decimal(item['amount'])
            yield item

    def add(self, donation):
        donation_id = str(donation.id)
        # if donation_id not in self.cart:
        self.cart[donation_id] = {'event': donation.event,
                                  'amount': donation.amount}

        self.save()

    def remove(self, donation):
        donation_id = str(donation.id)
        if donation_id in self.cart:
            del self.cart[donation_id]
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def clear(self):
        self.session[settings.CART_SESSION_ID] = {}
        self.session.modified = True

    def get_total_price(self):
        return sum(Decimal(item['amount']) for item in self.cart.values())
