from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')

def delivery(request):
    return render(request, 'main/delivery.html')

def pay(request):
    return render(request, 'main/pay.html')

def contacts(request):
    return render(request, 'main/contacts.html')

