from django.shortcuts import render, redirect
from .models import Caneta
from .forms import CanetaForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404

def home(request):
    return render(request,'cadastroCanetas/home.html')

def listaCanetas(request):
    
    canetas = Caneta.objects.order_by('data_added')
    context = {'canetas': canetas}
    return render(request,'cadastroCanetas/listaCanetas.html', context)

def novaCaneta(request):
    if request.method != 'POST':
        form = CanetaForm()
    
    else:
        form = CanetaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('listaCanetas'))
   
    context = {'form': form}
    return render(request, 'cadastroCanetas/novaCaneta.html', context)

def editarCaneta(request, caneta_id):
    caneta = get_object_or_404(Caneta, pk=caneta_id)

    if request.method == 'POST':
        form = CanetaForm(request.POST, instance=caneta)
        if form.is_valid():
            form.save()
            return redirect('listaCanetas')
    else:
        form = CanetaForm(instance=caneta)

    context = {'form': form, 'caneta': caneta}
    return render(request, 'cadastroCanetas/editarCaneta.html', context)

def excluirCaneta(request, caneta_id):
    caneta = get_object_or_404(Caneta, id=caneta_id)
    
    if request.method == 'POST':
        caneta.delete()
        return redirect('listaCanetas')  # redireciona após exclusão

    return render(request, 'cadastroCanetas/excluirCaneta.html', {'caneta': caneta})