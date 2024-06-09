from django import forms
from django import forms
from django.forms import ModelForm
from django.utils import timezone
from django.core.validators import MinValueValidator
from accounts.models.school_member import SchoolMember

class StuffForm(ModelForm):
    class Meta:
        model = SchoolMember
        fields = "__all__"
        exclude = ['parent', 'sibling', 'program']
        
        widgets = {
            "joining_date": forms.widgets.DateInput(attrs={"type": "date",}),
            "date_of_birth": forms.widgets.DateInput(attrs={"type": "date"}),
        }
        
    def __init__(self, *args, **kwargs):
        super(StuffForm, self).__init__(*args, **kwargs)

        
      
        self.fields['joining_date'].initial = timezone.now().date()
        self.fields['blood_group'].widget.attrs["class"] = "form-control select-2"
        
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"