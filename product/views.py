from django.shortcuts import render, HttpResponse
from .models import Vegetables


# Create your views here.
def homepage(request):
    #SELECT * FROM Vegetables
    product = Vegetables.objects.all()
    context = {'all_vegatles': product}
    return render(request, "product_1.html", context)

def catigories_view(request):
    pomidor_object = Vegetables.objects.get(id=1)
    description = pomidor_object.description
    return HttpResponse(description)

