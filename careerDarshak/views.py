from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from .forms import RegistrationForm,UserCreationForm

def home(request):
    return render(request, 'website/index.html')


def about(request):
    return render(request, 'website/about.html')


def contact(request):
    return render(request, 'website/contact.html')

def dashboard(request):
    return render(request, 'website/dashboard.html')

def fullresult(request):
    return render(request, 'website/fullresult.html')

class RegistrationView(View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, 'website/signup.html', {'form': form})
    
    def post(self, request):
        form =RegistrationForm(request.POST)
        if form.is_valid():
            # Save the user to the database
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login') 
        else:
            # If form is invalid, display errors
            messages.warning(request, 'Registration failed. Please correct the errors below.')
        return render(request, 'website/signup.html', {'form': form})

def privacy(request):
    return render(request, 'website/privacy.html')

def condition(request):
    return render(request, 'website/condition.html')