from django.shortcuts import render, redirect
from .models import Xunjian, Xunjian_result
from .forms import XunjianResultForm
from datetime import datetime
# Create your views here.

def XunjianList(request):
    # xunjian = Xunjian.objects.all()
    dayOfWeek = datetime.now().isoweekday()
    monthDay = datetime.now().day
    if dayOfWeek == 1 :
        xunjian = Xunjian.objects.filter(Weekly='1').order_by('suggestTime')
    elif monthDay == 1 :
        xunjian = Xunjian.objects.filter(Mothly='1').order_by('suggestTime')
    else:
        xunjian= Xunjian.objects.filter(daily='1').order_by('suggestTime')
    result = Xunjian_result.objects.all()
    return render(request, 'xunjian/xunjian_list.html', {'items':xunjian, 'results':result})

def xunjian_view(request):
    form = XunjianResultForm
    if request.method == 'POST':
        form = XunjianResultForm(request.POST)
        print(request.POST.dict())
        if form.is_valid():
            form.save()
            return redirect('xunjian_list')
    return render(request, 'xunjian/xunjian.html', {'form': form})