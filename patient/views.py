from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from patient.models import Patient
from django.template import loader
from django.urls import reverse

# Create your views here.

# view for displaying the data in a table
def patient(request):
    a=Patient.objects.all().values()
    template=loader.get_template('display_patient.html')
    context={'a':a,}
    
    return HttpResponse(template.render(context,request))


# view for displaying add.html or Form View
def add_patient(request):
    template=loader.get_template('add_patient.html')
    return HttpResponse(template.render({},request))


# view for adding record in a table
def addrecord(request):
    name=request.POST['name']
    age=request.POST['age']
    disease=request.POST['disease']
    status=request.POST['status']
    
    patient=Patient(name=name,age=age,disease=disease,status=status)
    patient.save()
    return HttpResponseRedirect(reverse('patient'))


def delete_patient(request,id):
    patient=Patient.objects.get(id=id)
    patient.delete()
    return HttpResponseRedirect(reverse('patient'))



def update_patient(request,id):
    patient=Patient.objects.get(id=id)
    template=loader.get_template('update_patient.html')
    context={'patient':patient,}
    return HttpResponse(template.render(context,request))


def updaterecord(request,id):
    name=request.POST['name']
    age=request.POST['age']
    disease=request.POST['disease']
    status=request.POST['status']
   
    patient=Patient.objects.get(id=id)
    
    patient.name=name
    patient.age=age
    patient.disease=disease
    patient.status=status
    
    patient.save()
    return HttpResponseRedirect(reverse('patient'))