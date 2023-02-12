
from django.contrib import admin
from django.urls import path
from pelanggaran.views import *
from django.contrib.auth.views import LoginView,LogoutView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('tambahkelas/',tambah_kelas,name='tambah_kelas'),
    path('tambahsiswa/',tambah_siswa,name='tambah_siswa'),
    path('tambahpelanggar/',tambah_pelanggar,name='tambah_pelanggar'),
    path('tambahpelanggaran/',tambah_pelanggaran,name='tambahpelanggaran'),
    path('pelanggaran/',pelanggaranpage,name="pelanggaranpage"),
    path('siswa/',siswa,name='siswa'),
    path('documentation/',documentation,name='documentation'),
    path('',pelanggaran,name='homepage'),
    path('adminpage/',adminpage,name='adminpage'),
    path('masuk/',LoginView.as_view(),name="masuk"),
    path('keluar/',LogoutView.as_view(),name="keluar"),
    path('detail/<int:id_siswa>',detail_siswa,name="detail_siswa"),
    path('pelanggaran/delete/<int:id_pelanggaran>',delete_pelanggaran,name="delete_pelanggaran"),
]
