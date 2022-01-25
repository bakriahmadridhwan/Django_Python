"""mysoft URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from software.views import *

urlpatterns = [
    path('software1/', include('software.urls')),
    path('admin/', admin.site.urls),
    path('software/', software, name="software"),
    path('tambah/', tambah),
    path('tambah-software/', tambah_software, name="tambah_software"),
    path('software/ubah/<int:id_software>', ubah_software, name='ubah_software'),
    path('software/hapus/<int:id_software>', hapus_software, name='hapus_software'),

]
