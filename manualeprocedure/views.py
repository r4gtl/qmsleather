from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from django.urls import reverse, reverse_lazy
from django.db.models import Sum, Count
import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import (Procedura, RevisioneProcedura, Modulo, RevisioneModulo
                    )
from .forms import ProceduraModelForm, RevisioneProceduraModelForm, ModuloModelForm
from .filters import ProceduraFilter

def procedure_home(request):
    procedure = Procedura.objects.all()
    procedura_filter = ProceduraFilter
    page = request.GET.get('page', 1)
    paginator = Paginator(procedure, 50)
    
    try:
        procedure_home = paginator.page(page)
    except PageNotAnInteger:
        procedure_home = paginator.page(1)
    except EmptyPage:
        procedure_home = paginator.page(paginator.num_pages)
    context={
        'procedure_home': procedure_home,
        'filter': procedura_filter,
        
    }
    return render(request, "manualeprocedure/procedure_home.html", context)




class ProceduraCreateView(LoginRequiredMixin,CreateView):
    model = Procedura
    form_class = ProceduraModelForm
    template_name = 'manualeprocedure/procedura.html'
    success_message = 'Procedura aggiunta correttamente!'
    #success_url = reverse_lazy('human_resources:human_resources')

    def get_success_url(self):        
        if 'salva_esci' in self.request.POST:
            return reverse_lazy('manualeprocedure:procedure_home')
        
        pk_procedura=self.object.pk
        return reverse_lazy('manualeprocedure:modifica_procedura', kwargs={'pk':pk_procedura})
    
    def form_valid(self, form):        
        messages.info(self.request, self.success_message) # Compare sul success_url
        return super().form_valid(form)
    
    def get_initial(self):
        created_by = self.request.user
        return {
            'created_by': created_by,
        }

class ProceduraUpdateView(LoginRequiredMixin, UpdateView):
    model = Procedura
    form_class = ProceduraModelForm
    template_name = 'manualeprocedure/procedura.html'
    success_message = 'Procedura modificata correttamente!'
    #success_url = reverse_lazy('human_resources:tabelle_generiche_formazione')
    
    def get_success_url(self):        
        if 'salva_esci' in self.request.POST:
            return reverse_lazy('manualeprocedure:procedure_home')
        
        pk_procedura=self.object.pk
        return reverse_lazy('manualeprocedure:modifica_procedura', kwargs={'pk':pk_procedura})
    

    def form_valid(self, form):        
        messages.info(self.request, self.success_message) # Compare sul success_url
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):        
        context = super().get_context_data(**kwargs)
        pk_procedura = self.object.pk        
        context['elenco_revisioni'] = RevisioneProcedura.objects.filter(fk_procedura=pk_procedura) 
        context['elenco_moduli'] = Modulo.objects.filter(fk_procedura=pk_procedura) 

        return context



def delete_procedura(request, pk): 
        deleteobject = get_object_or_404(Procedura, pk = pk)                 
        deleteobject.delete()
        url_match = reverse_lazy('manualeprocedure:procedure_home')
        return redirect(url_match)


class RevisioneProceduraCreateView(LoginRequiredMixin,CreateView):
    model = RevisioneProcedura
    form_class = RevisioneProceduraModelForm
    template_name = 'manualeprocedure/revisione_procedura.html'
    success_message = 'Revisione Procedura aggiunta correttamente!'
    #success_url = reverse_lazy('human_resources:human_resources')

    def get_success_url(self):   
        fk_procedura=self.object.fk_procedura.pk
        return reverse_lazy('manualeprocedure:modifica_procedura', kwargs={'pk':fk_procedura})
    
    def form_valid(self, form):        
        messages.info(self.request, self.success_message) # Compare sul success_url
        return super().form_valid(form)
    
    def get_initial(self):
        created_by = self.request.user
        fk_procedura = self.kwargs['pk']

        return {
            'created_by': created_by,
            'fk_procedura': fk_procedura
        }

    def get_context_data(self, **kwargs):        
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']       
        context['fk_procedura'] = Procedura.objects.get(pk=pk) 
        return context

class RevisioneProceduraUpdateView(LoginRequiredMixin, UpdateView):
    model = RevisioneProcedura
    form_class = RevisioneProceduraModelForm
    template_name = 'manualeprocedure/revisione_procedura.html'
    success_message = 'Revisione Procedura modificata correttamente!'
    #success_url = reverse_lazy('human_resources:tabelle_generiche_formazione')
    
    def get_success_url(self):        
        fk_procedura=self.object.fk_procedura.pk        
        return reverse_lazy('manualeprocedure:modifica_procedura', kwargs={'pk':fk_procedura})
    

    def form_valid(self, form):        
        messages.info(self.request, self.success_message) # Compare sul success_url
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):        
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']       
        context['fk_procedura'] = Procedura.objects.get(pk=pk)
        return context



def delete_revisione_procedura(request, pk): 
        deleteobject = get_object_or_404(RevisioneProcedura, pk = pk) 
        fk_procedura = deleteobject.fk_procedura.pk                
        deleteobject.delete()
        url_match = reverse_lazy('manualeprocedure:modifica_procedura', kwargs={'pk':fk_procedura})
        return redirect(url_match)



class ModuloCreateView(LoginRequiredMixin,CreateView):
    model = Modulo
    form_class = ModuloModelForm
    template_name = 'manualeprocedure/modulo.html'
    success_message = 'Modulo aggiunto correttamente!'
    #success_url = reverse_lazy('human_resources:human_resources')

    def get_success_url(self):   
        fk_procedura=self.object.fk_procedura.pk
        return reverse_lazy('manualeprocedure:modifica_procedura', kwargs={'pk':fk_procedura})
    
    def form_valid(self, form):        
        messages.info(self.request, self.success_message) # Compare sul success_url
        return super().form_valid(form)
    
    def get_initial(self):
        created_by = self.request.user
        fk_procedura = self.kwargs['pk']

        return {
            'created_by': created_by,
            'fk_procedura': fk_procedura
        }

    def get_context_data(self, **kwargs):        
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']       
        context['fk_procedura'] = Procedura.objects.get(pk=pk) 
        return context

class ModuloUpdateView(LoginRequiredMixin, UpdateView):
    model = Modulo
    form_class = ModuloModelForm
    template_name = 'manualeprocedure/modulo.html'
    success_message = 'Modulo modificato correttamente!'
    #success_url = reverse_lazy('human_resources:tabelle_generiche_formazione')
    
    def get_success_url(self):        
        fk_procedura=self.object.fk_procedura.pk        
        return reverse_lazy('manualeprocedure:modifica_procedura', kwargs={'pk':fk_procedura})
    

    def form_valid(self, form):        
        messages.info(self.request, self.success_message) # Compare sul success_url
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):        
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']       
        context['fk_procedura'] = Procedura.objects.get(pk=pk)
        return context



def delete_modulo(request, pk): 
        deleteobject = get_object_or_404(Modulo, pk = pk) 
        fk_procedura = deleteobject.fk_procedura.pk                
        deleteobject.delete()
        url_match = reverse_lazy('manualeprocedure:modifica_procedura', kwargs={'pk':fk_procedura})
        return redirect(url_match)
