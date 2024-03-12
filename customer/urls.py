from django.contrib import admin
from django.urls import path,include
from customer import views
from student import views as student_view

urlpatterns = [
    path('customer',views.customer,name="customer"),
    path('add_customer/',views.add_customer,name="add_customer"),
    path('add_customer/addrecord/',views.addrecord,name="addrecord"),
    path('delete_customer/<int:id>',views.delete_customer,name="delete"),
    path('update_customer/<int:id>',views.update_customer,name="update"),
    path('update_customer/updaterecord/<int:id>',views.updaterecord,name="updaterecord"),
    path('back',student_view.index,name="back"),
]
