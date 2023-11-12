from django import forms
from StaticFiles.model import Customers

class EmpForm(forms.ModelForm):
    class Meta:
        model=Customers

        fields = "_all_"