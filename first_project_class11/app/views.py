from django.shortcuts import render
from .models import Banner
# Create your views here.

def home(request):
    banner = Banner.objects.all()

    context = {
        'banner':banner
    }
    return render(request, 'app/index.html',context)
    