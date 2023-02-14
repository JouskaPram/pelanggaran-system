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
            point = req.POST['point'],

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
        petugas = User.objects.all()
        all = pelanggar.objects.all()
        langgar = pelanggar.objects.all().order_by('-id')
        total = all.count()
        user = petugas.count()
        konteks = {
            'langgar' : langgar,
            'total' : total,
            'user':user,
            
    }
        return render(req,'homepage.html',konteks)

def detail_siswa(req,id_siswa):
    
    nama = Siswa.objects.get(id=id_siswa)
    catatan = pelanggar.objects.filter(siswa=id_siswa)
    total = catatan.count()
    base = 100
    each = Pelanggaran.objects.filter(pelanggar__in=catatan).values("point")
    
    points = base
    if points < 0:
     points = 0
    elif points > 100:
     points = 100

    for item in each:
        points -= item["point"]
    if points < 50:
       pesan = "paggil orang tua"
    elif points > 50:
 
        pesan = "bersihin masjid"
    konteks = {'catatan' : catatan,
        'nama':nama,
        'total':total,
        'points':points,
        'pesan':pesan,
    }
    return render(req,'detail-pelanggar.html',konteks)

@login_required(login_url='masuk')
def adminpage(req):
    langgar = pelanggar.objects.all().count()
    nama = Siswa.objects.all()
    total = nama.count()
    petugas = User.objects.all().count()
    kelas = Kelas.objects.all().count()
    catatan = pelanggar.objects.values("siswa")
    result = Pelanggaran.objects.filter(pelanggar__in=catatan).values("point")
    points = 100
    if points < 0:
     points = 0
    elif points > 100:
     points = 100

    for item in result:
        points -= item["point"]
    if points < 50:
       pesan = "bahaya"
    elif points > 50:
        
        pesan = "aman"
    

    konteks ={
        'nama':nama,
       'total':total,
       'petugas':petugas,
       'langgar':langgar,
       'kelas':kelas,
       'result': result,
       'pesan':pesan
    
    }
    return render(req,'adminpage.html',konteks)


@login_required(login_url='masuk')
def pelanggaranpage(req):
    all = Pelanggaran.objects.all()
    konteks = {
        'all':all
    }
    return render(req,'pelanggaran.html',konteks)
    
@login_required(login_url='masuk')
def delete_pelanggaran(req,id_pelanggaran): 
    nama = Pelanggaran.objects.filter(id=id_pelanggaran)
    nama.delete()
    messages.success(req,"data berhasil di hapus")  
    return redirect('/pelanggaran/')

@login_required(login_url='masuk')
def documentation(req):
    return render(req,'documentation.html')

