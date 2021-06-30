from django.shortcuts import render, HttpResponse, resolve_url
from django.contrib import messages

from datetime import datetime
from homepage.models import Contact

# Create your views here.
def index(request):
    
    return render(request=request, template_name='index.html')
    
def about(request):
    return render(request=request, template_name='about.html')

def solutions(request):
    return render(request=request, template_name='solutions.html')

def contact(request):

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        date = datetime.today()
        
        contact = Contact(name= name, email=email, phone = phone, desc= desc, date = date)
        contact.save()
        messages.success(request, 'Your Request has been submitted.')

    return render(request=request, template_name='contact.html')