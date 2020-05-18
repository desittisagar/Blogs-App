from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy

# Create your views here.

class SignUp(CreateView):
	form_class = UserCreationForm
	template_name = 'signup.html'
	success_url = reverse_lazy('login')