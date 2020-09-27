from django.shortcuts import render
from .forms import StaffCreateForm

# Create your views here.
def registrationStaff(request):

    form_obj = StaffCreateForm()

    if request.method == "POST":

        form_obj = StaffCreateForm(request.POST)

        if form_obj.is_valid():
            form_obj.save()
            form_obj = StaffCreateForm()


    context ={

        "reg_form": form_obj

    }
    return render(request, 'StaffManagement/registration.html', context)



