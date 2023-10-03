from django.shortcuts import render,redirect
from todoapp.forms import create_task
from todoapp.models import task

# Create your views here.

def create(request):
    form = create_task()
    
    if request.method == "POST":
        form = create_task(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        

    data = task.objects.order_by("-id")


    context = {'form':form,'data':data}
    return render(request,'create.html',context)



def dele(request,id):
    da= task.objects.get(id=id)
    da.delete()
    return redirect('/')


def edi(request,id):
    dat=task.objects.get(id=id)
    context = {'data':dat}
    if request.method=='POST':
        form = create_task(request.POST,instance=dat)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'update.html',context)

def com_task(request,id):
    tsk=task.objects.get(id=id)
    tsk.complete = True if request.GET.get('complete') == 'true' else False
    tsk.save()
    
    return redirect('/')


