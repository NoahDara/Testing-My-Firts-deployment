from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, FormView, DetailView
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
from accounts.models.school_member import SchoolMember
from .forms import UserCreationForm, UserUpdateForm
from django.contrib.auth.views import PasswordResetView
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.views.generic import FormView
from django.contrib.auth.hashers import make_password
from django.views.generic.edit import UpdateView
from .forms import LoginForm

class SchoolMemberListView(SuccessMessageMixin, ListView):
    model = SchoolMember
    context_object_name = 'school_members'
    queryset = SchoolMember.objects.all()
    # paginate_by = 25
    template_name = "accounts/school_member/list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context
    
class SchoolMemberDetailView(SuccessMessageMixin,DetailView):
    model = SchoolMember
    context_object_name = 'school_member'
    template_name = 'accounts/school_member/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context    

User = get_user_model()

class LoginUserView(FormView):
    template_name = "registration/login.html"
    form_class = LoginForm
    success_url = reverse_lazy("dashboard")

    def form_valid(self, form):
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
            messages.success(
                self.request, f"You have successfully logged in as: {user.username}"
            )
            return super().form_valid(form)
        else:
            messages.warning(
                self.request, "Please check your credentials and try again"
            )
            return redirect("login")

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect(self.success_url)
        return super().dispatch(request, *args, **kwargs)


class UserListView(ListView):
    model = User
    template_name = "registration/index.html"


def register_user(request):
    if request.method == "GET":
        return render(request, "registration/create.html", {"form": UserCreationForm()})
    elif request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User created successfully")
            return redirect("users-index")
        else:
            messages.error(request, "Something went wrong. Please try again.")
            return render(request, "registration/create.html", {"form": form})



class UserUpdateView(SuccessMessageMixin, UpdateView):
    model = User
    template_name = "registration/update.html"
    form_class = UserUpdateForm
    success_message = "User updated successfully"

    def get_success_url(self):
        return reverse("users-index")

    def form_valid(self, form):
            # Get the existing user object
            user = get_object_or_404(User, pk=self.kwargs['pk'])
            # Update the user object with the form data
            user.member = form.cleaned_data['member']
            # Save the updated user object
            user.save()
            return super().form_valid(form)

class UserDeleteView(DeleteView):
    model = User
    success_message = "User deleted successfully"

    def get_success_url(self):
        return reverse("users-index")

class CustomPasswordResetView(PasswordResetView):
    email_template_name = "account/password_reset_email.html"
    html_email_template_name = "account/password_reset_email.html"

    def send_mail(
        self,
        subject_template_name,
        email_template_name,
        context,
        from_email,
        to_email,
        html_email_template_name=None,
    ):
        html_email = render_to_string(html_email_template_name, context)
        email_message = EmailMessage(
            subject_template_name,
            html_email,
            from_email,
            [to_email],
        )

        email_message.content_subtype = "html"
        email_message.send()


def custom_logout(request):
    if request.user.is_authenticated and request.method == 'GET':
        logout(request)
    return redirect('login')