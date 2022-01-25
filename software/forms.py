from django.forms import ModelForm
from django import forms
from software.models import Software

class FormSoftware(ModelForm):
    class Meta:
        model = Software
        fields = "__all__"
        # exclude = ["judul"]

        widgets = {
            'judul': forms.TextInput({'class': 'form-control'}),
            'deskripsi': forms.TextInput({'class': 'form-control'}),
            'os': forms.TextInput({'class': 'form-control'}),
        }