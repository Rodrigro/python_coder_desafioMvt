from django.http import HttpResponse
from django.shortcuts import render
from Personas.models import Familiares 




def create_parent (request):
    Familiares.objects.create(name='Roberto Esteban Gimenez', identification= 23456789, is_parent=False)
    Familiares.objects.create(name='Juan Perez', identification= 29843333, is_parent=True)

    
    return HttpResponse('Nuevo Familiar Agregado ')

def list_parents(request):
    all_parents = Familiares.objects.all()
    context = {
        'persona':all_parents,
    }
    return render(request, 'list_familiares.html', context=context)
    
