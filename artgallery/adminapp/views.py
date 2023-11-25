from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound
from django.shortcuts import redirect
from .models import Product
from customerapp.models import Feedback
from artistapp.models import Artist
from artistapp.forms import ArtistForm
from customerapp.models import Address
from artistapp.models import ArtistRequest
from django.shortcuts import render, get_object_or_404
from .forms import ProductForm

@login_required(login_url='login')
def adminhome(request):
    products = Product.objects.all()
    return render(request, 'adminapp/adminhome.html', {'products': products})

def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        product.delete()
        return render(request,'adminapp/adminhome.html')
    return render(request,'adminapp/adminhome.html')

def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('adminhome')
    else:
        form = ProductForm(instance=product)
    return render(request, 'adminapp/edit.html', {'form': form})

def upload_product(request):
    if request.method == 'POST':
        title = request.POST['title']
        price = request.POST['price']
        image = request.FILES['image']
        Product.objects.create(title=title, price=price, image=image)
        return redirect('adminhome')
    return render(request, 'adminapp/uploadopt.html')

def logout(request):
    return render(request,"login.html")

def feedbackpage(request):
    data=Feedback.objects.all()
    return render(request,'adminapp/feedbacks.html',{'data':data})

def add_artist(request):
    if request.method == "POST":
        form = ArtistForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_artist')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    print(f"Field: {field}, Error: {error}")
    else:
        form = ArtistForm()
    artists = Artist.objects.all()
    return render(request, 'adminapp/artistdata.html', {'form': form, 'artists': artists})

def delete_artist(request):
    if request.method == "POST":
        username = request.POST.get('username')
        try:
            artist = Artist.objects.get(username=username)
            artist.delete()
            return redirect('add_artist')
        except Artist.DoesNotExist:
            return HttpResponseNotFound('Artist not found')
    return redirect('add_artist')

def orders(request):
    addresses = Address.objects.all()
    return render(request,'adminapp/orders.html',{'addresses': addresses})

def requests(request):
    artist_requests = ArtistRequest.objects.all()
    return render(request,'adminapp/requests.html', {'artist_requests': artist_requests})
