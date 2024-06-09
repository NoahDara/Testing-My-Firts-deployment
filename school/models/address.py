from django.db import models


class CountryField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 100)
        super().__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        from django_countries.fields import CountryField as DjangoCountryField
        defaults = {'form_class': DjangoCountryField}
        defaults.update(kwargs)
        return super().formfield(**defaults)

class Address(models.Model):

    address_line1 = models.CharField(max_length=255)
    address_line1= models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = CountryField()

    def __str__(self):
        return f"{self.city}-{self.country}"