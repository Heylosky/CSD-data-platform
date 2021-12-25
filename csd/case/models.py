from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=40)
    def __str__(self):
        return self.name

class Rfo(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    def __str__(self):
        return self.name

class Onduty(models.Model):
    name = models.CharField(max_length=15)
    def __str__(self):
        return self.name

class Provider(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name
    
class Fault(models.Model):
    name = models.CharField(max_length=35)
    def __str__(self):
        return self.name

class TicketNumber(models.Model):
    tktnumber = models.CharField(max_length=124)
    product_ID = models.CharField(max_length=12)
    service = models.ForeignKey(Service, on_delete=models.DO_NOTHING, blank=False, null=False)
    priority = models.CharField(max_length=5, choices=(('P1','P1'),('P2','P2'),('P3','P3'),('P4','P4')))
    provider = models.ForeignKey(Provider, on_delete=models.DO_NOTHING, blank=False, null=False)
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING, blank=False, null=False)
    fault = models.ForeignKey(Fault, on_delete=models.DO_NOTHING, blank=False, null=False)
    rfo = models.ForeignKey(Rfo, on_delete=models.DO_NOTHING, blank=False, null=False)
    TTR = models.IntegerField(blank=False, null=False)
    First_response_time = models.IntegerField(blank=False, null=False)
    closedate = models.DateTimeField(auto_now_add=True, editable=True)
    onduty = models.ForeignKey(Onduty, on_delete=models.DO_NOTHING, blank=False, null=False)
    fix_by_csd = models.CharField(max_length=5, choices=(('YES','YES'),('NO','NO')), null=True, blank=True)
    
    # service = models.ForeignKey(Service, on_delete=models.DO_NOTHING, blank=False, null=False)
    # rfo = models.ForeignKey(Rfo, on_delete=models.DO_NOTHING, blank=False, null=False)    

    def __str__(self):
        return self.tktnumber
