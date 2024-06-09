from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from accounts.views import  UserListView, UserUpdateView, UserDeleteView, LoginUserView, SchoolMemberListView, SchoolMemberDetailView
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [

    path('users-index', UserListView.as_view(), name="users-index"),
    path('register-user', views.register_user, name="register-user"),
    path('update-user/<int:pk>/', UserUpdateView.as_view(), name="update-user"),
    path('delete-user/<int:pk>/', UserDeleteView.as_view(), name="delete-user"),

    path("school-member/", SchoolMemberListView.as_view(), name="school-member-list"),
    path("school-member/details/<int:pk>", SchoolMemberDetailView.as_view(),name="school-member-details",),

    # user authentication
    path('', LoginUserView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='account/password_reset.html'), name='password_reset_request'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='account/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='account/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='account/password_reset_complete.html'), name='password_reset_complete'),
    path('custom_logout/', views.custom_logout, name='logout'),
]