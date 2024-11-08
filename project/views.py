from django.shortcuts import render
from django.views import View

# Create your views here.

class projectdashboardview(View):
    def get(self,request):
        return render(request,'pdash.html')
    
class Addprojectview(View):
    def get(self,request):
        return render(request,'addproject.html')