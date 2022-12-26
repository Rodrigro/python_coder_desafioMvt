from django.http import HttpResponse
from django.shortcuts import render
from Personas.models import Familiares 




def create_parent (request):
    Familiares.objects.create(name='Juacito Esteban Gimenez', identification= 23456789, is_parent=False)
    Familiares.objects.create(name='Juan Perez', identification= 29843333, is_parent=True)
    Familiares.objects.create(name='Marina Alfonso', identification= 34843333, is_parent=True)


    #Familiares.objects.filter(name__contains='Juancito').delete()
    
    return HttpResponse('Nuevo Familiar Agregado ')

def list_parents(request):
    all_parents = Familiares.objects.all()
    context = {
        'persona':all_parents,
    }
    return render(request, 'list_familiares.html', context=context)
    
def delete_all(request):
    Familiares.objects.all().delete()
    return HttpResponse('Todos Borrado') 