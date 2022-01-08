from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User ,auth
# Create your views here.
from module.models import product, bill


def load_login(request):

    if request.user.is_authenticated:
        return redirect("home")

    if request.method=='POST':
        username = request.POST['email']
        password = request.POST['pass']

        ispresent=auth.authenticate(username=username,password=password)
        if ispresent is not None:
            auth.login(request, ispresent)
            return redirect("home")
        else:
            messages.info(request,'Invalid credentials TRY AGAIN!!!')
            return render(request, 'Login.html')


    return render(request,'Login.html')

def load_logout(request):
    auth.logout(request)
    return render(request,'login.html')
def home(request):
    pros = product.objects.all()

    return render(request, 'home.html', {'proli': pros})

def get_chartdata(request):

    obj=bill.objects.all()
    labels=list()
    datalist = list()
    for item in obj:
        date=str(item.date)
        dt1=date.split()
        finaldate=dt1[0]
        profit=item.profit
        labels.append(finaldate)
        datalist.append(profit)

    data={
        "response_labels":labels,
        "response_data":datalist
    }
    return JsonResponse(data)