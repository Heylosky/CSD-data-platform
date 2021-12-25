from django.db import models
from case.models import Onduty

# Create your models here.
class Xunjian(models.Model):
    xunjian_items = models.CharField(max_length=32)
    web = models.CharField(max_length=128, blank=True, null=True)
    suggestTime = models.TimeField()
    daily = models.BooleanField()
    weekly = models.BooleanField()
    monthly = models.BooleanField()
    def __str__(self):
        return self.xunjian_items
    
class Xunjian_result(models.Model):
    item = models.ForeignKey(Xunjian, on_delete=models.DO_NOTHING, blank=False, null=False)
    onduty = models.ForeignKey(Onduty, on_delete=models.DO_NOTHING, blank=False, null=False)
    result = models.CharField(max_length=10, choices=(('OK','OK'),('Resolve','Resolve'),('Fault','Fault'),('Warning','Warning')))
    check_time = models.DateTimeField(auto_now_add=True, editable=True)