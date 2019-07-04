from django.shortcuts import render
from  django.http import HttpResponse
from .forms import Addform
def index(request):
    if request.method=='POST':
        form =Addform(request.POST)
        if form.is_valid():
            a=form.cleaned_data['a']
            b=form.cleaned_data['b']
            return HttpResponse(str(int(a)+int(b)))
    else:
        form=Addform()
    return render(request,'blog/index.html',{'form':form})

# Create your views here.
