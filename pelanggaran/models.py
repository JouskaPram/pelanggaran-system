from django.db.models import *

# Create your models here.
class Kelas(Model):
    nama_kelas = CharField(max_length=40)
    def __str__(self):
        return(self.nama_kelas)
class Siswa(Model):
    nisn = IntegerField()
    nama_siswa = CharField(max_length=50)
    kelas = ForeignKey(Kelas,on_delete=CASCADE)
    def __str__(self):
        return(self.nama_siswa)
class Pelanggaran(Model):
    jenis_pelanggaran= TextField()
    def __str__(self):
        return(self.jenis_pelanggaran)

class pelanggar(Model):
    tanggal = DateTimeField(auto_now=True)
    siswa = ForeignKey(Siswa,on_delete=CASCADE)
    pelanggaran = ForeignKey(Pelanggaran,on_delete=CASCADE)
    def __str__(self):
        return self.siswa.nama_siswa