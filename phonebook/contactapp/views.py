from django.shortcuts import render
from .models import Phonebook

# Create your views here.

def home(request):
    return render(request,"index.html")

def addphone(request):
    responseDic={}
    try:
        Name=request.POST['name']
        Phone=int(request.POST['phone'])

        phnlist=Phonebook.objects.filter(name=Name)
        if phnlist.exists():
            responseDic["key"]="Already exists"
            return render(request,"index.html",responseDic)
        else:
            phnlist=Phonebook(name=Name,phone=Phone)
            phnlist.save()
        responseDic["key"]="Phone Number is added"
        return render(request,"index.html",responseDic)
    except Exception as p:
        print(p)
        responseDic["key"]="Phone Number is not added"
        return render(request, "index.html",responseDic)

def display(request):
    phndis=Phonebook.objects.all()
    return render(request,"index.html",{'phn':phndis})

def delete(request):
    try:
        Name=request.POST['name']
        phndel=Phonebook.objects.filter(name=Name)
        phndel.delete()
        return render(request,"index.html",{'key1':"Deleted"})
    except Exception as p:
        print(p)
        return render(request,"index.html",{'key1':"Not Deleted"})

def update(request):
    try:
        oldname=request.POST["oldname"]
        newname=request.POST['newname']
        Phonebook.objects.filter(name=oldname).update(name=newname)
        return render(request,"index.html",{'key2':"Updated"})
    except Exception as p:
        return render(request,"index.html",{'key2':"Not Updated"})