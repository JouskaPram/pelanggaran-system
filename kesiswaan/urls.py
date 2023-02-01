
from django.contrib import admin
from django.urls import path
from pelanggaran.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('tambahkelas/',tambah_kelas,name='tambah_kelas'),
    path('tambahsiswa/',tambah_siswa,name='tambah_siswa'),
    path('',tambah_pelanggar,name='tambah_pelanggar'),
    path('siswa/',siswa,name='siswa'),
    path('pelanggar/',pelanggaran,name='pelanggar'),
]
