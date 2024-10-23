from django.shortcuts import render,redirect
from datetime import datetime
from home.models import Contact
from home.forms import support 
from django.contrib import messages # Updated to use the correct model class name

# Create your views here.
def index(request):
   
    return render(request, 'index.html')
    # return HttpResponse("this is homepage")

def about(request):
    return render(request, 'about.html')
    # return HttpResponse("this is about page")

def services(request):
    return render(request, 'services.html')
    # return HttpResponse("this is services page")

def contact(request):
    if request.method == "POST":
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        contact = Contact(fullname=fullname, email=email, phone=phone, message=message, date=datetime.today())
        contact.save()
        return redirect('ty')
    return render(request, 'contact.html')
    # return HttpResponse("this is contact page")

def ty(request):
    return render(request,'ty.html')

def services2(request):
    if request.method == 'POST':
        form = support(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            messages.success(request, "Your form has been submitted")  # Show success message
            return redirect('services2')  # Redirect to the same page to clear the form data and prevent resubmission
    else:
        form = support()
    
    return render(request, 'services2.html', {'form': form})
    return render(request, 'services2.html', {'form': form})
def services3(request):
    return render(request,'services3.html')
    