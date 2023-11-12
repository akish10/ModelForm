from django.shortcuts import render
from staticFilesHandling.form import StuForm


# Create your views here.
def index(request):
    stu= EmpForm()
    return render(request,'index.html',{'form':stu})