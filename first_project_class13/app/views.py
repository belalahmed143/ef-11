from django.shortcuts import render,redirect
from .models import *
from .forms import *
# Create your views here.

def home(request):
    banner = Banner.objects.all()
    services = Service.objects.all()
    cate1_service = Service.objects.filter(category__name='Cate-1')
    cate2_service = Service.objects.filter(category__name='Cate-2')
    exact_data = Service.objects.filter(title__exact='Service-1')
    iexact_data = Service.objects.filter(title__iexact='Service-1')
    contains_data = Service.objects.filter(description__contains='d')
    in_data = Service.objects.filter(title__in = ['service-2'])
    gt_data = Service.objects.filter(id__gte = 2)

    context = {
        'banner':banner,
        'services':services,
        'cate1_service':cate1_service,
        'cate2_service':cate2_service,
        'exact_data':exact_data,
        'iexact_data':iexact_data,
        'contains_data':contains_data,
        'in_data':in_data,
        'gt_data':gt_data
    }
    return render(request, 'app/index.html',context)
    

# def contact(request):
#     form = ConatctForm()
#     if request.method == 'POST':
#         form = ConatctForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     context ={
#         'form':form
#     }
#     return render(request,'app/contact.html',context)


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        submit = ContactUs(name=name,email=email,message=message)
        submit.save()
        return redirect('/')
    return render(request,'app/contact.html')
    