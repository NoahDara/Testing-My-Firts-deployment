from django import forms
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import  Group
from django.contrib.auth.forms import UserCreationForm
from accounts.models import SchoolMember, User


class UserCreationForm(UserCreationForm):
    member = forms.ModelChoiceField(queryset=SchoolMember.objects.all(), label='SchoolMember')
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ("member",)

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            role = self.cleaned_data.get('member').role
            try:
                group = Group.objects.get(name=role)
            except Group.DoesNotExist:
                group = None
            if group:
                user.groups.add(group)  

        # Set user fields based on selected member
        member = self.cleaned_data['member']
        user.first_name = member.first_name
        user.last_name = member.last_name
        user.email = member.email
        
        if commit:
            user.save()  
        return user
        
        
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            "username",     
            "first_name",
            "last_name",
            "email",
            "groups",
        )
        exclude = ["password"]

    class Meta:
        model = User
        fields = ('member', 'groups')

class LoginForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
