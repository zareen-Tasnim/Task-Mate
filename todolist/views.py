from django.core import paginator
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from todolist.models import Tasklist
from todolist.forms import TaskForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

@login_required
def todolist(request):
    if request.method == "POST":
        form =TaskForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit = False)
            instance.manage = request.user
            instance.save()
        return redirect('todolist')
    else:
        all_tasks=Tasklist.objects.filter(manage=request.user)
        paginator= Paginator(all_tasks,5)
        page = request.GET.get("pg")
        all_tasks=paginator.get_page(page)
        return render(request, 'todolist.html', {'all_tasks': all_tasks})

def delete_task(request,task_id):
    task = Tasklist.objects.get(pk=task_id)
    if task.manage == request.user:
        task.done = True
        task.delete()
    else:
        print("Access Restricted")
    return redirect('todolist')


def complete_task(request,task_id):
    task = Tasklist.objects.get(pk=task_id)
    if task.manage == request.user:
        task.done = True
        task.save()

    else:
        print("Access Restricted")
 
    return redirect('todolist')


def pending_task(request,task_id):
    task = Tasklist.objects.get(pk=task_id)
    if task.manage == request.user:
        task.done = False
        task.save()

    else:
        print("Access Restricted")

    return redirect('todolist')

   

def edit_task(request,task_id):
    if request.method == "POST":
        task = Tasklist.objects.get(pk=task_id)
        form =TaskForm(request.POST or None, instance = task)
        if form.is_valid():
            form.save()
        return redirect('todolist')
    else:
        task_obj = Tasklist.objects.get(pk=task_id)
        return render(request, 'edit.html', {'task_obj':task_obj})

@login_required
def contact(request):
    all_tasks=Tasklist.objects.all
    return render(request, 'contact.html', {'Welcome_text':'Welcome to Contact Us'})


def home(request):
    all_tasks = Tasklist.objects.all
    return render(request, 'home.html', {'Welcome_text':'Welcome to Home-Page'})