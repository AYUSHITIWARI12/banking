from django.shortcuts import render, HttpResponse


def bankHome(request):
    return render(request,'bank/bankHome.html')
