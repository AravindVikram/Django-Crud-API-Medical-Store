from django.db import models
from datetime import timedelta

class medicine(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=255)
    expiry_date = models.DateField(null=True)
    code = models.CharField(max_length=50)
    company = models.CharField(max_length=255, default="company")
    confirm_company = models.CharField(max_length=255, default="company")

    def update_expiry_date(self):
        if self.expiry_date:
            self.expiry_date += timedelta(days=365)

    def save(self, *args, **kwargs):
        self.code += '_med@store'
        self.update_expiry_date()
        super(medicine, self).save(*args, **kwargs)

    def compare_company(self):
        return self.company == self.confirm_company
    