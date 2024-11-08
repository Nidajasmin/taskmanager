from django.shortcuts import render,redirect
from django.views import View
from .forms import taskForm
from django.http import HttpResponse
from .models import Task


# Create your views here.

# def Lnadingview(request):
#   return render(request,'landing.html')

class LandingView(View):
   def get(self,request):
    return render(request,'landing.html')


# def dashboardview(request):
#   return render(request,'dashboard.html')

class DashboardView(View):
   def get(self,request):
    data=Task.objects.all()
    return render(request,'dash.html',{'data':data})
   
class AddTaskView(View):
  def get(self,request):
    forms=taskForm()
    return render(request,'add.html',{'form':forms})
  
  def post(self,request):
    forms_data=taskForm()
    forms_data=taskForm(data=request.POST)
    if forms_data.is_valid():
       title=forms_data.cleaned_data.get('title')
       description=forms_data.cleaned_data.get('description')
       date=forms_data.cleaned_data.get('date')
       time=forms_data.cleaned_data.get('time')
       Task.objects.create(title=title,description=description,date=date,time=time)
       return redirect('dashboard')
    return render(request,'add.html',{'form':forms_data})
  
class deletetaskview(View):
  def get(self,request,*args,**kwargs):
    ti=kwargs.get('id')
    print('ti')
    task=Task.objects.get(id=ti)
    task.delete()
    return redirect('dashboard')
  

class edittaskview(View):
  def get(self,request,**kwargs):
    ti=kwargs.get('id')
    task=Task.objects.get(id=ti)
    forms=taskForm(initial={'title':task.title,'description':task.description,'date':task.date,'time':task.time})
    return render(request,'edit.html',{'form':forms})
  
  def post(self,request,**kwargs):
    forms_data=taskForm(data=request.POST)
    ti=kwargs.get('id')
    task=Task.objects.get(id=ti)
    if forms_data.is_valid():
      title=forms_data.cleaned_data.get('title')
      description=forms_data.cleaned_data.get('description')
      date=forms_data.cleaned_data.get('date')
      time=forms_data.cleaned_data.get('time')
      task.title=title
      task.description=description
      task.date=date
      task.time=time
      task.save()
      return redirect('dashboard')
    return render(request,'edit.html',{'form':forms_data})






    