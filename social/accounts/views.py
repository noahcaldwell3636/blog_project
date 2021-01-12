from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.views.generic.base import TemplateView

from . import forms

# Create your views here.
class sign_up(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'


class logged_out(TemplateView):
    template_name= 'accounts/logout.html'


class my_account(TemplateView):
    template_name= 'accounts/my_account.html'