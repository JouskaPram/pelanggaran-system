from django.forms import ModelForm
from .models import *
from django import forms


class FormSiswa(ModelForm):
    class Meta:
        model= Siswa
        fields = "__all__"

class FormPelanggar(ModelForm):
    class Meta:
        model = pelanggar
        fields = "__all__"

    # widget ={
    #     'Siswa' : forms.Select({'class':'form-control'}),
    # }