from django.contrib import admin
from django.urls import path,include
from student import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student',views.student,name="student"),
    path('add/',views.add,name="add"),
    path('add/addrecord/',views.addrecord,name="addrecord"),
    path('delete/<int:id>',views.delete,name="delete"),
    path('update/<int:id>',views.update,name="update"),
    path('update/updaterecord/<int:id>',views.updaterecord,name="updaterecord"),
    path('',views.index,name="index"),
    path('back',views.index,name="index"),
    
    
]
