from django.shortcuts import render, redirect
from .models import GarageModel
from .forms import GarageForm


# Create your views here.
def index(request):
    Items = GarageModel.objects.all()
    return render(request, 'BootCRUDApp/index.html', {'Items': Items})


def newItem(request):
    form = GarageForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("index")

    return render(request, 'BootCRUDApp/newItem.html', {'form': form})
