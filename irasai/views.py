from django.shortcuts import render, get_object_or_404
from .models import Artistas, Irasas
from django.views import generic
from django.db.models import Q
# from django.http import HttpResponse


def index(request):
    num_irasai = Irasas.objects.all().count()
    num_artistai = Artistas.objects.count()

    context_t = {
        'num_irasai_t': num_irasai,
        'num_artistai_t': num_artistai,
    }

    return render(request, 'index.html', context=context_t)


def artistai(request):
    artistai_visos_eilutes = Artistas.objects.all()
    # print(authors)
    context_t = {
        'artistai_visos_eilutes_t': artistai_visos_eilutes
    }
    return render(request, 'artistai_visi.html', context=context_t)

