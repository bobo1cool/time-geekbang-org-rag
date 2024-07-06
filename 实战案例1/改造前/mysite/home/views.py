from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse

from .models import 销售入账记录

def index(request):
    # return HttpResponse("home index")
    return render(request, "home/index.html")

def salescheck(request):
    # return HttpResponse("home index")
    if request.method == 'POST':
        print(request.POST)
    else:
        object_list = 销售入账记录.objects.all()

    return render(request, "home/salescheck.html",context={"object_list":object_list})

def addsalescheck(request):
    if request.method == 'POST':
        record = 销售入账记录()
        record.客户 = request.POST['name']
        record.入账日期 = request.POST['created_at']
        record.入账金额 = request.POST['amount']
        record.已到账款项 = request.POST['total']
        record.剩余到账款项 = request.POST['leave']

        record.save()
        return redirect(reverse('home:salescheck'))
    else:
        return render(request, "home/addsalescheck.html")
