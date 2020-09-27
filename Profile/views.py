from django.shortcuts import render
from .forms import CreateUserCreateForm

# Create your views here.
def Userregistration(request):

    form_obj = CreateUserCreateForm()

    if request.method == "POST":

        form_obj = CreateUserCreateForm(request.POST)

        if form_obj.is_valid():
            form_obj.save()


    context ={

        "reg_form": form_obj

    }
    return render(request, 'Profile/userregistration.html', context)

