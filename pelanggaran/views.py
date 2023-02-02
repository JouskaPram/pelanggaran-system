from django.shortcuts import *
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required(login_url='masuk')
def tambah_kelas(req):
    if req.POST:
        Kelas(
            nama_kelas = req.POST['nama_kelas'],

        ).save()
    return render(req,'tambah-kelas.html')
@login_required(login_url='masuk')
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
@login_required(login_url='masuk')
def tambah_pelanggar(req):
    if req.POST:
     form = FormPelanggar(req.POST,instance=pelanggar(user=req.user))
     if form.is_valid:
        form.save()
        form = FormPelanggar()
        messages.success(req,"data berhasil di tambahkan")
        konteks = {
            'form':form,
        }
        return redirect("/tambahpelanggar",konteks)
    else:
        form = FormPelanggar()
        konteks ={
            'form':form
        }
        return render(req,'pelanggar.html',konteks)
@login_required(login_url='masuk')
def siswa(req):
    siswa = Siswa.objects.all()
    konteks ={
        'siswa' : siswa
    }
    return render(req,'siswa.html',konteks)
@login_required(login_url='masuk')
def pelanggaran(req):
    all = pelanggar.objects.all()
    if req.POST:
        keyword = req.POST['cari']
        langgar = pelanggar.objects.filter(siswa__nama_siswa__contains=keyword).order_by('-id')[:10]
        total = all.count()
        konteks = {
            'langgar':langgar,
            'total':total           
        }
        
    else:
        all = pelanggar.objects.all()
        langgar = pelanggar.objects.all().order_by('-id')[:10]
        total = all.count()
        konteks = {
            'langgar' : langgar,
            'total' : total,
            
    }
    return render(req,'langgar.html',konteks)

def detail_siswa(req,id_siswa):
   
    nama = Siswa.objects.get(id=id_siswa)
    catatan = pelanggar.objects.filter(siswa=id_siswa)
    total = catatan.count()
    if total<10:
        pesan = 'membersihkan masjid'
    elif total>10:
        pesan = 'panggil orang tua'
    else:
        pesan = 'tidak ada'
    konteks = {'catatan' : catatan,
        'nama':nama,
        'total':total,
        'pesan':pesan
  
    }
    return render(req,'detail-pelanggar.html',konteks)