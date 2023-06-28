from django.shortcuts import render,redirect
from rest_framework import mixins
from rest_framework import generics
from .models import User, Customer, Campany, Subject, TicketSupport
from .serializers import (CustomerSerializer,CompanySerializer, SubjectSerializer)
from .forms import CustomerForm, CampanyForm, SubjectForm, TicketForm
from django.contrib import messages
  


 
# partials web fucitonlite

def create_subject(request):
    
    context ={}
    context["tickets"] = TicketSupport.objects.all()
    context["companies"] = Campany.objects.all()
 
    # add the subject
    form = TicketForm(request.POST or None)
    form_s = SubjectForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, f"Add succefuly")
    if form_s.is_valid():
        form_s.save()
        messages.success(request, f"Add succefuly")
         
    context['form']= form
    context['form_s']= form_s
    return render(request, "create_subject.html", context)

# add customer
def save_customer(request):
    if request.method == 'POST':
        email= request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        username = request.POST.get('username')
       
        customer = Customer(email=email, phone_number=phone_number,username=username)
        customer.save()
        messages.success(request, f"Add succefuly")
        return redirect('create_subject')
    
# function  
def save_campany(request):
    if request.method == 'POST':
        name= request.POST.get('campany_name')
       
        campany = Campany(name=name)
        
        campany.save()
        messages.success(request, f"Add succefuly")

        return redirect('create_subject')
    
# function sa ticket 
def save_ticket(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        support = request.POST.get('assignee')
        status = request.POST.get('status')
        description = request.POST.get('description')
        suject = request.POST.get('suject')
        
        
        tickets = TicketSupport(title=title,assignee=support,status=status,description=description,suject=suject)
        
        tickets.save()
        messages.success(request, f"Add succefuly")

        return redirect('create_subject')
    
def save_subject(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        company = request.POST.get('company')
        
        
        tickets = Subject(title=title,company=company)
        
        tickets.save()
        messages.success(request, f"Add succefuly")

        return redirect('create_subject')


def create_customer(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    form = CustomerForm(request.POST or None)
    if form.is_valid():
        form.save()
         
    context['form']= form
    return render(request, "create_customer.html", context)


def create_campany(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    form = CampanyForm(request.POST or None)
    if form.is_valid():
        form.save()
         
    context['form']= form
    return render(request, "create_campany.html", context)


# partials for api   
# view for User 
class CustomerList(generics.ListCreateAPIView):
    
    queryset =Customer.objects.all()
    serializer_class = CustomerSerializer


# view for Campany
class CampanyList(generics.ListCreateAPIView):
    
    queryset = Campany.objects.all()
    serializer_class = CompanySerializer

# view for subject   
class SubjectList(generics.ListCreateAPIView):
    
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
  
