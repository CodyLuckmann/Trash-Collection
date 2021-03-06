from django.apps import apps
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from datetime import date, datetime
from customers.models import Customer
from .models import Employee


# Create your views here.

# TODO: Create a function for each path created in employees/urls.py. Each will need a template as well.


def index(request):
    # This line will get the Customer model from the other app, it can now be used to query the db for Customers
    Customer = apps.get_model('customers.Customer')
    return render(request, 'employees/index.html')

@login_required
def index(request):
    # The following line will get the logged-in user (if there is one) within any view function
    logged_in_user = request.user
    try:
        # This line will return the customer record of the logged-in user if one exists
        logged_in_employee = Employee.objects.get(user=logged_in_user)
        all_customers = Customer.objects.all()
        day_of_week = datetime.today().strftime('%A')
        today = date.today()
       
        
        
        
        context = {
            'logged_in_employee': logged_in_employee,
            'today': today,
            'all_customers': all_customers,
            'day_of_week': day_of_week
        }
        return render(request, 'employees/index.html', context)
    except ObjectDoesNotExist:
        return HttpResponseRedirect(reverse('employees:create'))
    

@login_required
def create(request):
    logged_in_user = request.user
    if request.method == "POST":
        name_from_form = request.POST.get('name')
        address_from_form = request.POST.get('address')
        zip_from_form = request.POST.get('zip_code')
        new_employee = Employee(name=name_from_form, user=logged_in_user, address=address_from_form, zip_code=zip_from_form)
        new_employee.save()
        return HttpResponseRedirect(reverse('employees:index'))
    else:
        return render(request, 'employees/create_employee.html')
    
@login_required
def edit_profile(request):
    logged_in_user = request.user
    logged_in_employee = Employee.objects.get(user=logged_in_user)
    if request.method == "POST":
        name_from_form = request.POST.get('name')
        address_from_form = request.POST.get('address')
        zip_from_form = request.POST.get('zip_code')
        logged_in_employee.name = name_from_form
        logged_in_employee.address = address_from_form
        logged_in_employee.zip_code = zip_from_form
        logged_in_employee.save()
        return HttpResponseRedirect(reverse('employees:index'))
    else:
        context = {
            'logged_in_employee': logged_in_employee
        }
        return render(request, 'employees/edit_employee_profile.html', context)
    
def charge(request, pk):
    
    customer = Customer.objects.get(id=pk)
    customer.balance+=20
    customer.date_of_last_pickup = date.today()
    customer.save()
    return HttpResponseRedirect(reverse('employees:index'))


def filter_monday(request):
    all_customers = Customer.objects.all()
    context = {
        'all_customers': all_customers
    }
    return render(request, 'employees/monday.html', context)

def filter_tuesday(request):
   all_customers = Customer.objects.all()
    
   context = {
        'all_customers': all_customers
   }
   return render(request, 'employees/tuesday.html', context)

def filter_wednesday(request):
   all_customers = Customer.objects.all()
    
   context = {
        'all_customers': all_customers
    }
   return render(request, 'employees/wednesday.html', context)

def filter_thursday(request):
    all_customers = Customer.objects.all()
    
    context = {
        'all_customers': all_customers
    }
    return render(request, 'employees/thursday.html', context)

def filter_friday(request):
    all_customers = Customer.objects.all()
    
    context = {
        'all_customers': all_customers
    }
    return render(request, 'employees/friday.html', context)
