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
from student.forms.student import StudentForm



class StudentListView(LoginRequiredMixin, ListView):
    model = SchoolMember
    context_object_name = "students"
    template_name = "student/student/list.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class StudentCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = SchoolMember
    form_class = StudentForm
    template_name = "student/student/create.html"
    success_message = "Student created successfully"

    def get_success_url(self):
        return reverse("student-index")


class StudentDetailsView(LoginRequiredMixin, DetailView):
    model = SchoolMember
    context_object_name = "students"
    template_name = "student/student/details.html"


class StudentUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = SchoolMember
    context_object_name = "students"
    template_name = "student/student/update.html"
    form_class = StudentForm
    success_message = "Student successfully"

    def get_success_url(self):
        return reverse("student-index")


class StudentDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = SchoolMember
    template_name = "student/student/delete.html"
    success_message = "Studentdeleted successfully"

    
    def get_success_url(self):
        return reverse("student-index")