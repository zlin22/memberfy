from django.db import models
import datetime


class MembershipConfig(models.Model):
    org_id = models.CharField(max_length=100)
    price_plan_id = models.CharField(max_length=255, blank=True, null=True)
    days_valid = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255, null=True)
    banner_message = models.CharField(max_length=255, null=True)
    is_displayed_on_site = models.BooleanField(
        verbose_name="Is displayed for purchase", default=True)
    is_subscription = models.BooleanField(default=False)
    display_order = models.IntegerField(default=1)


class Membership(models.Model):
    membership_config_id = models.CharField(max_length=100)
    user_id = models.CharField(max_length=100)
    initiation_date = models.DateField(null=True, blank=True)
    expiration_date = models.DateField(null=True, blank=True)
    payment_status = models.CharField(max_length=100)

    @property
    def is_active(self):
        return (self.expiration_date or datetime.date(2000, 1, 1)) >= datetime.date.today()


class AuxMembership(models.Model):
    membership_id = models.CharField(max_length=100)
    user_id = models.CharField(max_length=100)
