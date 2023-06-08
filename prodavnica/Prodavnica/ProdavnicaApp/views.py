from django.shortcuts import render, redirect
from .forms import FoodForm
from .models import Product

# Create your views here.

def index(request):
    return render(request,"index.html")

def outofstock(request):
    if request.method == 'POST':
        data = FoodForm(data=request.POST, files=request.FILES)
        if data.is_valid():
            product = data.save(commit=False)

            # Set the user for the product based on the logged-in user
            product.user = request.user  # Assuming user authentication is enabled

            # Save the product to the database
            product.save()
            return redirect("outofstock")

    objects = Product.objects.filter(quantity__gt=0).all()
    context = {"products": objects, "form": FoodForm}
    return render(request,"outofstock.html",context = context)