from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.models import *
from app.forms import *
def insert_student(request):
    SFO=StudentForm()
    d={'SFO':SFO}
    if request.method=='POST':
        SFDO=StudentForm(request.POST)
        if SFDO.is_valid():
            sname=SFDO.cleaned_data['sname']
            sid=SFDO.cleaned_data['sid']
            semail=SFDO.cleaned_data['semail']
            SO=Student.objects.get_or_create(sname=sname,sid=sid,semail=semail)[0]
            SO.save()
            SDDO=Student.objects.all()
            a={'SDDO':SDDO}
            return render(request,'display_students.html',a)
    return render(request,'insert_student.html',d)