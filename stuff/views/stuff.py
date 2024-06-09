from django.shortcuts import render, redirect
from django.views.generic import (
    TemplateView,
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

from accounts.models.school_member import SchoolMember
from stuff.forms.stuff import StuffForm



class StuffListView(LoginRequiredMixin, ListView):
    model = SchoolMember
    context_object_name = "stuff"
    template_name = "stuff/stuff/list.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class StuffCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = SchoolMember
    form_class = StuffForm
    template_name = "stuff/stuff/create.html"
    success_message = "stuff created successfully"

    def get_success_url(self):
        return reverse("stuff-index")


class StuffDetailsView(LoginRequiredMixin, DetailView):
    model = SchoolMember
    context_object_name = "stuff"
    template_name = "stuff/stuff/details.html"


class StuffUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = SchoolMember
    context_object_name = "stuffs"
    template_name = "stuff/stuff/update.html"
    form_class = StuffForm
    success_message = "stuff successfully"

    def get_success_url(self):
        return reverse("stuff-index")


class StuffDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = SchoolMember
    template_name = "stuff/stuff/delete.html"
    success_message = "stuffdeleted successfully"

    
    def get_success_url(self):
        return reverse("stuff-index")