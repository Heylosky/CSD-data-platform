from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import TicketCreationForm
from .models import TicketNumber, Rfo

from django.views.generic import ListView

class ticket_list_view(ListView):
    model = TicketNumber
    context_object_name = 'tickets'
    template_name = "case/ticketnumber_list.html"
    def get_queryset(self):                       # 重写get_queryset方法
        return TicketNumber.objects.all().order_by('-closedate')

def ticket_create_view(request):
    form = TicketCreationForm()
    if request.method == 'POST':
        form = TicketCreationForm(request.POST)
        print(request.POST.dict())
        if form.is_valid():
            form.save()
            return redirect('ticket_list')
    return render(request, 'case/add_ticket.html', {'form': form})


def ticket_update_view(request, pk):
    ticket = get_object_or_404(TicketNumber, pk=pk)
    form = TicketCreationForm(instance=ticket)
    if request.method == 'POST':
        form = TicketCreationForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            # return redirect('person_change', pk=pk)
            return redirect('ticket_list')
    return render(request, 'case/add_ticket.html', {'form': form})


# AJAX
def load_tickets(request):
    service_id = request.GET.get('service_id')
    rfos = Rfo.objects.filter(service_id=service_id).all().order_by('name')
    return render(request, 'case/rfo_dropdown_list_options.html', {'rfos': rfos})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)
