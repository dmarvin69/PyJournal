from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    context = {
    "values": ["Test 1", "Test 2"]
    }
    #return HttpResponse("Hello World!")
    return render(request, "main/index.html",context)

# templates/main/index.html
