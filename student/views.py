from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from student.models import Student
from django.template import loader
from django.urls import reverse

# Create your views here.

def index(request):
    return render(request,'index.html')


# view for displaying the data in a table
def student(request):
    a=Student.objects.all().values()
    template=loader.get_template('display.html')
    context={'a':a,}
    
    return HttpResponse(template.render(context,request))


# view for displaying add.html or Form View
def add(request):
    template=loader.get_template('add.html')
    return HttpResponse(template.render({},request))


# view for adding record in a table
def addrecord(request):
    name=request.POST['name']
    age=request.POST['age']
    mobile=request.POST['mobile']
    address=request.POST['address']
    
    student=Student(name=name,age=age,mobile=mobile,address=address)
    student.save()
    return HttpResponseRedirect(reverse('student'))


def delete(request,id):
    student=Student.objects.get(id=id)
    student.delete()
    return HttpResponseRedirect(reverse('student'))



def update(request,id):
    student=Student.objects.get(id=id)
    template=loader.get_template('update.html')
    context={'student':student,}
    return HttpResponse(template.render(context,request))


def updaterecord(request,id):
    name=request.POST['name']
    age=request.POST['age']
    mobile=request.POST['mobile']
    address=request.POST['address']
    
    student=Student.objects.get(id=id)
    
    student.name=name
    student.age=age
    student.mobile=mobile
    student.address=address
    
    
    student.save()
    return HttpResponseRedirect(reverse('student'))