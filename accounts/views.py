from django.shortcuts import redirect, render 
from django.http import request
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def sign_up(request):
    form = UserCreationForm
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")

    return render(request, 'accounts/sign_up.html', context={'form':form})