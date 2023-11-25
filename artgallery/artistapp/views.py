from django.shortcuts import render, redirect
from adminapp.models import Product
from customerapp.forms import AddressForm
from .forms import ArtistRequestForm

def artisthome(request):
    products = Product.objects.all()
    return render(request,"artistapp/artisthome.html",{'products': products})

def artistlogout(request):
    return render(request,"login.html")

def artistupload(request):
    if request.method == 'POST':
        title = request.POST['title']
        price = request.POST['price']
        image = request.FILES['image']
        Product.objects.create(title=title, price=price, image=image)
        return redirect('artisthome')
    return render(request, 'artistapp/artistupload.html')

def artistabout(request):
    return render(request,'artistapp/artistabout.html')

def requestpage(request):
    if request.method == 'POST':
        form = ArtistRequestForm(request.POST)
        msg="Your request was sent successfully!!"
        if form.is_valid():
            form.save()
            return render(request,'artistapp/request.html',{'form':form,'msg':msg})
    else:
        form = ArtistRequestForm()
    return render(request, 'artistapp/request.html', {'form': form})

def artistaddress(request, title, price):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            form.instance.price = price
            form.instance.title = title
            form.save()
            return redirect('artistpaymentpage', price=price, title=title)
    else:
        form = AddressForm(initial={'price': price, 'title': title})
    return render(request, 'artistapp/artistaddress.html', {'form': form, 'price': price, 'title': title})

def artistpaymentpage(request,price,title):
    if request.method == 'POST':
        return render(request,'artistapp/artistpaymentsuccess.html',{'price': price, 'title': title})
    return render(request,'artistapp/artistpaymentpage.html',{'price': price, 'title': title})

