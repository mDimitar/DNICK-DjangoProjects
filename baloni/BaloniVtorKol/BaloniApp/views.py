from django.shortcuts import render, redirect
from .forms import FlightForm
from .models import Fligth

# Create your views here.

def index(request):
    return render(request,"index.html")


def flights(request):
    if request.method == 'POST':
        data = FlightForm(data=request.POST, files=request.FILES)
        if data.is_valid():
            flight = data.save(commit=False)
            flight.user = request.user
            flight.image = data.cleaned_data['image']
            flight.save()
            return redirect("flights")

    objects = Fligth.objects.filter(user=request.user, airportNameDepart="Skopje").all()
    context = {"flights": objects, "form": FlightForm}
    return render(request,"flights.html",context = context)
