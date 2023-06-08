from django.shortcuts import render,redirect
from .models import Repair
from .forms import RepairForm

# Create your views here.

def index(request):
    return render(request,"index.html")

def repairs(request):
    if request.method == "POST":
        form_data = RepairForm(data=request.POST, files=request.FILES)
        if form_data.is_valid():
            repair = form_data.save(commit=False)
            repair.user = request.user
            repair.date = form_data.cleaned_data['date']
            repair.image = form_data.cleaned_data['image']
            repair.save()
            return redirect("repairs")
    data = Repair.objects.filter(user = request.user.id ,car__type = "Sedan").all()
    context = {"repairs": data,"form": RepairForm}
    return render(request,"repairs.html",context=context)
