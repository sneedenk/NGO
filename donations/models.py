from django.db import models
from users.models import User


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

    donor = models.ForeignKey(Donor, on_delete=models.CASCADE)
    donation_type = models.CharField(max_length=40, null=False, blank=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)


class Events(models.Model):
    name = models.CharField(max_length=40, null=False, blank=False)
    date = models.DateField(null=False, blank=False)
