from django.forms import ModelForm
from .models import *
from django import forms
from django.contrib.auth.models import User

class FormSiswa(ModelForm):
    class Meta:
        model= Siswa
        fields = "__all__"

class FormPelanggar(ModelForm):
    class Meta:
        model = pelanggar
        exclude = ('user',)

        widgets = {
            'siswa': forms.Select(attrs={'class': 'form-control'}),
            'pelanggaran': forms.Select(attrs={'class': 'form-control'}),

        }
    