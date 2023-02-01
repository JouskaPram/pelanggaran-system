from django.shortcuts import render,redirect
from .models import *
from .forms import *
def tambah_kelas(req):
    if req.POST:
        Kelas(
            nama_kelas = req.POST['nama_kelas'],

        ).save()
    return render(req,'tambah-kelas.html')

def tambah_siswa(req):
    if req.POST:
     form = FormSiswa(req.POST)
     if form.is_valid:
        form.save()
        form = FormSiswa
        konteks = {
            'form':form,
        }
        return render(req,'tambahsiswa.html',konteks)
    else:
        form = FormSiswa()
        konteks ={
            'form':form
        }
        return render(req,'tambahsiswa.html',konteks)
# add pelanggar
def tambah_pelanggar(req):
    if req.POST:
     form = FormPelanggar(req.POST)
     if form.is_valid:
        form.save()
        form = FormPelanggar
        konteks = {
            'form':form,
        }
        return redirect("/pelanggar")
    else:
        form = FormPelanggar()
        konteks ={
            'form':form
        }
        return render(req,'pelanggar.html',konteks)

def siswa(req):
    siswa = Siswa.objects.all()
    konteks ={
        'siswa' : siswa
    }
    return render(req,'siswa.html',konteks)

def pelanggaran(req):
    
    if req.POST:
        keyword = req.POST['cari']
        langgar = pelanggar.objects.filter(siswa__nama_siswa__contains=keyword).order_by('-id')
        total = langgar.count()
        konteks = {
            'langgar':langgar,
            'total':total,
        }
        return render(req,'langgar.html',konteks)
    else:
        
        langgar = pelanggar.objects.all().order_by('-id')
        total = langgar.count()
        konteks = {
            'langgar' : langgar,
            'total' : total,
    }
    return render(req,'langgar.html',konteks)