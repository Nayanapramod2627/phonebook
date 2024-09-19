from django.urls import path
from.import views

urlpatterns=[
    path('',views.home),
    path('phonebook',views.addphone),
    path('display',views.display),
    path('delete',views.delete),
    path('update',views.update)
]