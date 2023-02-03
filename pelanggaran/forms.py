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
            'siswa': forms.Select(attrs={'class': 'form-control select2 '}),
            'pelanggaran': forms.Select(attrs={'class': 'form-control select2'}),
            'nisn': forms.NumberInput(attrs={'class': 'form-control'}),
            'nama_siswa': forms.TextInput(attrs={'class': 'form-control'}),
            'kelas': forms.TextInput(attrs={'class': 'form-control'}),
            'nama_kelas': forms.TextInput(attrs={'class': 'form-control'}),
         

        }
    