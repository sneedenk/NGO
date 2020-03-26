# Generated by Django 3.0.4 on 2020-03-26 02:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CMA_num', models.IntegerField()),
                ('phone', models.CharField(max_length=40)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=40)),
                ('state', models.CharField(max_length=40)),
                ('zip_code', models.CharField(max_length=40)),
                ('country', models.CharField(max_length=40)),
                ('urbanization', models.CharField(blank=True, max_length=40, null=True)),
                ('date', models.DateField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DonationDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donation_type', models.CharField(max_length=40)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('donor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='donations.Donor')),
            ],
        ),
        migrations.AddConstraint(
            model_name='donationdetails',
            constraint=models.UniqueConstraint(fields=('donor', 'donation_type'), name='unique_donation'),
        ),
    ]
