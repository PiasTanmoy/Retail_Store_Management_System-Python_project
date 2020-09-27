from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm


def InsertCustomer(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')


    context ={

        'form' : form
    }
    return render(request, 'registration/register.html',context)