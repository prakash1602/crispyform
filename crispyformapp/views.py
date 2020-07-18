from django.shortcuts import render,redirect
from .models import StudentDetails
from .forms import StudentDataForm
from django.http.response import HttpResponse

# Create your views here.
def Student_data(request):
    form=StudentDataForm()
    context={'form':form}
    if request.method=='POST':
        form=StudentDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('data')
    return render(request,'studentdata.html',context)
def Fetching_data(request):
    data=StudentDetails.objects.all()
    context={'data':data}
    return render(request,'studentdata.html',context)


