from django.db import models
import datetime
from django.utils import timezone


class detrack(models.Model):
    datee=models.DateField()
    crde=models.CharField(max_length=100)
    whrerwhom=models.CharField(max_length=100)
    howmuch=models.CharField(max_length=100)

    class Meta:
        db_table = "dettable"
