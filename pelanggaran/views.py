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
def tambah_pelanggaran(req):
    if req.POST:
        Pelanggaran(
            jenis_pelanggaran = req.POST['jenis_pelanggaran'],

        ).save()
        messages.success(req,"data berhasil di tambahkan")
        return redirect('/tambahpelanggaran')
    else:
      
        return render(req,'tambah-pelanggaran.html')
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

def pelanggaran(req):
        all = pelanggar.objects.all()
        langgar = pelanggar.objects.all().order_by('-id')
        total = all.count()
        konteks = {
            'langgar' : langgar,
            'total' : total,
            
    }
        return render(req,'homepage.html',konteks)

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

@login_required(login_url='masuk')
def adminpage(req):
    nama = Siswa.objects.all()

    konteks ={
        'nama':nama,
       
    }
    return render(req,'adminpage.html',konteks)

