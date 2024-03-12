from django.contrib import admin
from django.urls import path,include
from patient import views
from student import views as student_view

urlpatterns = [
    path('patient',views.patient,name='patient'),
    path('add_patient/',views.add_patient,name="add_customer"),
    path('add_patient/addrecord/',views.addrecord,name="addrecord"),
    path('delete_patient/<int:id>',views.delete_patient,name="delete_patient"),
    path('update_patient/<int:id>',views.update_patient,name="update_patient"),
    path('update_patient/updaterecord/<int:id>',views.updaterecord,name="updaterecord"),
    path('back',student_view.index,name="back"),
]
