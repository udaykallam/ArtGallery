from django.http import JsonResponse
import re
from .models import Feedback
from adminapp.models import Product
from .forms import AddressForm
from django.shortcuts import render, redirect


def contactfunction(request):
    if request.method == "POST":
        name = request.POST.get('n')
        phone = request.POST.get('number')
        email = request.POST.get('mail')
        feedback = request.POST.get('feed')
        if len(phone) > 10 or len(phone)<10:
            m2 = "Phone number should be 10 digits."
            return render(request, "customerapp/contact.html", {"msgm2": m2})
        elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            m3 = "Invalid email address. Please enter a valid email."
            return render(request, "customerapp/contact.html", {"msgm3": m3})
        else:
            contact = Feedback(name=name, phone=phone, email=email, feedback=feedback)
            contact.save()
            m1 = "Your Feedback Was Sent Successfully!!"
            return render(request, "customerapp/contact.html", {"msgm1": m1})

    return render(request, "customerapp/contact.html")

def greeting(request):
    return render(request,"customerapp/greeting.html")

def search_view(request):
    query = request.GET.get('q', '')
    products = Product.objects.filter(title__icontains=query)
    print(f"Search Query: {query}")
    print(f"Number of Products Found: {products.count()}")
    context = {
        'products': products,
        'query': query,
    }
    return render(request, 'customerapp/search_results.html', context)

def search_view1(request):
    query = request.GET.get('q', '')
    products = Product.objects.filter(title__icontains=query)
    print(f"Search Query: {query}")
    print(f"Number of Products Found: {products.count()}")
    context = {
        'products': products,
        'query': query,
    }
    return render(request, 'customerapp/search_results1.html', context)

def search_suggestions(request):
    query = request.GET.get('q', '')
    products = Product.objects.filter(title__icontains=query).values_list('title', flat=True)
    suggestions = list(products)
    return JsonResponse({'suggestions': suggestions})

def address(request, title, price):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            form.instance.price = price
            form.instance.title = title
            form.save()
            return redirect('paymentpage', price=price, title=title)
    else:
        form = AddressForm(initial={'price': price, 'title': title})
    return render(request, 'customerapp/address.html', {'form': form, 'price': price, 'title': title})

def message(request):
    products=Product.objects.all()
    return render(request,'customerapp/message.html',{'products':products})

def paymentpage(request,price,title):
    if request.method == 'POST':
        return render(request,'customerapp/paymentsuccess.html',{'price': price, 'title': title})
    return render(request,'customerapp/paymentpage.html',{'price': price, 'title': title})

