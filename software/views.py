from re import template
from django.shortcuts import render, redirect
from django.http import HttpResponse
from software.models import Software
from software.forms import FormSoftware
from django.contrib import messages

# Create your views here.

def index(request):

    judul = "Software1"

    konteks = {
        "title": judul
    }

    return HttpResponse("Halo..!", konteks)

def software(request):

    judul = "Website Daftar Software"


    soft = Software.objects.all()

    konteks = {
        "title": judul,
        "software" : soft
    }

    return render(request, "software.html", konteks)

def tambah(request):

    judul = "Tambah"

    konteks = {
        "title": judul
    }

    return render(request, "tambah.html", konteks)


def tambah_software(request):

    if request.POST:
        form = FormSoftware(request.POST)
        if form.is_valid():
            form.save()
            form = FormSoftware()
            pesan = "Data berhasil disimpan..!"

            konteks = {
                "form" : form,
                "pesan" : pesan,
            }
            return render(request, "tambah_software.html", konteks)
    else:
        form = FormSoftware()

        konteks = {
            "form" : form,
        }

    return render(request, "tambah_software.html", konteks)


def ubah_software(request, id_software):

    software = Software.objects.get(id = id_software)
    template = 'ubah-software.html'
    if request.POST:
        form = FormSoftware(request.POST, instance = software)
        if form.is_valid():
            form.save()
            messages.success(request, "Data berhasil diubah..!")

            return redirect('ubah_software', id_software = id_software)
    else:
        form = FormSoftware(instance = software)
        konteks = {
            'form': form,
            'soft' : software,
        }
    return render(request, template, konteks)


def hapus_software(request, id_software):
    software = Software.objects.filter(id=id_software)
    software.delete()
    messages.success(request, "Data berhasil dihapus..!")

    return redirect('software')


