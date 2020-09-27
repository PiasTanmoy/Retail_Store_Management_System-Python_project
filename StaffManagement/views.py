from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def registrationStaff(request):
    form = UserCreationForm()

    if request.method == 'post':
        form = UserCreationForm(request.post)
        if form.is_valid():
            form.save()

    context = {
        'form': form
    }

    return render(request, "StaffManagement/registration.html", context)



