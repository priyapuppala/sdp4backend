from django import forms
from .models import *


class OrphanageForm(forms.ModelForm):
    class Meta:
        model = Orphanage
        fields = "__all__"
        # widgets = {
        #     'password': forms.PasswordInput(),
        # }
