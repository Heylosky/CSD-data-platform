from django import forms

from case.models import TicketNumber, Rfo, Customer, Fault, Provider


class TicketCreationForm(forms.ModelForm):
    class Meta:
        model = TicketNumber
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['rfo'].queryset = Rfo.objects.none()
        self.fields['customer'].queryset = Customer.objects.all().order_by('name')
        self.fields['fault'].queryset = Fault.objects.order_by('name')
        self.fields['provider'].queryset = Provider.objects.order_by('name')
        if 'service' in self.data:
            try:
                service_id = int(self.data.get('service'))
                self.fields['rfo'].queryset = Rfo.objects.filter(service_id=service_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['rfo'].queryset = self.instance.service.rfo_set.order_by('name')
