from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib import messages
from django.contrib.auth import login, authenticate


def register(request):
    form = RegistrationForm

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created for ' + form.cleaned_data.get('username'))
            return redirect('login')

    context = {'form': form}
    return render(request, 'registration/register.html', context)

def dashboard(request):
    return render(request, 'dashboard.html')