from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import CustomRegisterForm
from django.contrib import messages


# Create your views here.
def register(request):
    if request.method=="POST":
        register_form = CustomRegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request,"NEW USER CREATED SUCCESSFULLY!")
            return redirect("todolist")
    else:
        register_form = CustomRegisterForm()
    return render(request, 'register.html', {'register_form':register_form})
    

