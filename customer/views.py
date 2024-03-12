from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from customer.models import Customer
from django.template import loader
from django.urls import reverse

# Create your views here.

# view for displaying the data in a table
def customer(request):
    a=Customer.objects.all().values()
    template=loader.get_template('display_customer.html')
    context={'a':a,}
    
    return HttpResponse(template.render(context,request))


# view for displaying add.html or Form View
def add_customer(request):
    template=loader.get_template('add_customer.html')
    return HttpResponse(template.render({},request))


# view for adding record in a table
def addrecord(request):
    name=request.POST['name']
    mobile=request.POST['mobile']
    address=request.POST['address']
    purchased_items=request.POST['purchased_items']
    payable_amount=request.POST['payable_amount']
    
    customer=Customer(name=name,mobile=mobile,address=address,purchased_items=purchased_items,payable_amount=payable_amount)
    customer.save()
    return HttpResponseRedirect(reverse('customer'))


def delete_customer(request,id):
    customer=Customer.objects.get(id=id)
    customer.delete()
    return HttpResponseRedirect(reverse('customer'))



def update_customer(request,id):
    customer=Customer.objects.get(id=id)
    template=loader.get_template('update_customer.html')
    context={'customer':customer,}
    return HttpResponse(template.render(context,request))


def updaterecord(request,id):
    name=request.POST['name']
    mobile=request.POST['mobile']
    address=request.POST['address']
    purchased_items=request.POST['purchased_items']
    payable_amount=request.POST['payable_amount']
    
    customer=Customer.objects.get(id=id)
    
    customer.name=name
    customer.mobile=mobile
    customer.address=address
    customer.purchased_items=purchased_items
    customer.payable_amount=payable_amount
    
    
    customer.save()
    return HttpResponseRedirect(reverse('customer'))