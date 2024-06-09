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
from guardian.forms.guardian import GuardianForm



class GuardianListView(LoginRequiredMixin, ListView):
    model = SchoolMember
    context_object_name = "guardians"
    template_name = "guardian/guardian/list.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class GuardianCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = SchoolMember
    form_class = GuardianForm
    template_name = "guardian/guardian/create.html"
    success_message = "Student Guardian created successfully"

    def get_success_url(self):
        return reverse("guardian-index")


class GuardianDetailsView(LoginRequiredMixin, DetailView):
    model = SchoolMember
    context_object_name = "guardians"
    template_name = "guardian/guardian/details.html"


class GuardianUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = SchoolMember
    context_object_name = "guardians"
    template_name = "guardian/guardian/update.html"
    form_class = GuardianForm
    success_message = "Student Guardian successfully"

    def get_success_url(self):
        return reverse("guardian-index")


class GuardianDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = SchoolMember
    template_name = "guardian/guardian/delete.html"
    success_message = "Guardian deleted successfully"

    
    def get_success_url(self):
        return reverse("guardian-index")