from django.shortcuts import render,redirect
from base.models import *

# Create your views here.
def home(request):
    success =False
    if request.method == 'POST':
        
        title= request.POST.get('title')
        desc= request.POST.get('desc')
        
        ins = Tasks(title=title,description=desc)
        ins.save()
        success=True
    return render(request, 'base/home.html',{'success':success})
def tasks(request):
    my_tasks = Tasks.objects.all()
    context = {'tasks':my_tasks}
    return render(request, 'base/tasks.html',context)
def delete(request,t_id):
    del_task =Tasks.objects.get(id=t_id)
    del_task.delete()
    return redirect( 'tasks')
def update(request, u_id):
    task = Tasks.objects.get(id=u_id)

    if request.method == 'POST':
        return redirect('doupdtasks', u_id=u_id)  # Redirect to form processing view

    return render(request, 'base/update.html', {'task': task})

def doupdate(request, u_id):
    task = Tasks.objects.get(id=u_id)

    if request.method == 'POST':
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        task.title = title
        task.description = desc
        task.save()

        return redirect('tasks')

    return render(request, 'base/update.html', {'task': task})

    # If GET request, render an update form
    return render(request, 'base/update_task.html', {'task': upd_task})
