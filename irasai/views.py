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


def artistas(request, artistas_id):
    artistas_viena_eilute = get_object_or_404(Artistas, pk=artistas_id)
    context_t = {
        'artistas_viena_eilute_t': artistas_viena_eilute
    }
    return render(request, 'artistas_vienas.html', context=context_t)


### klases tipo views. ListView - visom eilutem

class IrasasListView(generic.ListView): # ListView - visos eilutės (objektai)
    model = Irasas # modelioklasė_list -> irasas_list
    context_object_name = 'irasas_list'
    template_name = 'irasai_visi.html'


### klases tipo views. DetailView - vienos eilutes
class IrasasDetailView(generic.DetailView):
    model = Irasas
    context_object_name = 'irasas'
    template_name = 'irasas_vienas.html'


# paieska viewsas

def search(request):
    paieskos_tekstas = request.GET.get('laukelio-tekstas')
    paieskos_rezultatai = Irasas.objects.filter(
        Q(albumas__icontains=paieskos_tekstas) |
        Q(artistasFK__pavadinimas__icontains=paieskos_tekstas)
    )
    # print(request.GET)
    # search_results = Book.objects.filter(
    #     Q(title__icontains=query) |
    #     Q(summary__icontains=query)
    # )
    # context_t = {
    #     'query_t': query,
    #     'search_results_t': search_results
    # }
    context_t = {
        'paieskos_tekstas_t': paieskos_tekstas,
        'paieskos_rezultatai_t': paieskos_rezultatai
    }
    return render(request, 'paieskos-rezultatai.html', context=context_t)

