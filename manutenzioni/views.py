from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from django.urls import reverse, reverse_lazy
from django.db.models import Sum, Count
import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages


from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import (Attrezzatura, ManutenzioneStraordinaria,
                    ManutenzioneOrdinaria, Taratura
                    )
from .forms import AttrezzaturaModelForm, ManutenzioneOrdinariaModelForm, ManutenzioneStraordinariaModelForm, TaraturaModelForm
from .filters import AttrezzaturaFilter



def dashboard_manutenzioni(request):
    attrezzature = Attrezzatura.objects.filter(is_dismesso=False)
    filter = AttrezzaturaFilter(request.GET, queryset=Attrezzatura.objects.all())
    manutenzioni_ordinarie = ManutenzioneOrdinaria.objects.all()
    manutenzioni_straordinarie = ManutenzioneStraordinaria.objects.all()
    tarature = Taratura.objects.all()
    filterset_class = AttrezzaturaFilter
    page = request.GET.get('page', 1)
    paginator = Paginator(attrezzature, 50)
    
    try:
        attrezzature_home = paginator.page(page)
    except PageNotAnInteger:
        attrezzature_home = paginator.page(1)
    except EmptyPage:
        attrezzature_home = paginator.page(paginator.num_pages)
    context={
        'attrezzature_home': attrezzature_home,
        'filter': filter,
        'manutenzioni_ordinarie': manutenzioni_ordinarie,
        'manutenzioni_straordinarie': manutenzioni_straordinarie,
        'tarature': tarature
    }
    return render(request, "manutenzioni/dashboard_manutenzioni.html", context)



class AttrezzaturaCreateView(LoginRequiredMixin,CreateView):
    model = Attrezzatura
    form_class = AttrezzaturaModelForm
    template_name = 'manutenzioni/attrezzatura.html'
    success_message = 'Attrezzatura aggiunta correttamente!'
    #success_url = reverse_lazy('human_resources:human_resources')

    def get_success_url(self):     
        if 'salva_esci' in self.request.POST:
            return reverse_lazy('manutenzioni:dashboard_manutenzioni')
        
        pk_attrezzatura=self.object.pk
        return reverse_lazy('manutenzioni:modifica_attrezzatura', kwargs={'pk':pk_attrezzatura})   
        
        
        
    
    def form_valid(self, form):        
        messages.info(self.request, self.success_message) # Compare sul success_url
        return super().form_valid(form)
    
    def get_initial(self):
        created_by = self.request.user
        return {
            'created_by': created_by,
        }

class AttrezzaturaUpdateView(LoginRequiredMixin, UpdateView):
    model = Attrezzatura
    form_class = AttrezzaturaModelForm
    template_name = 'manutenzioni/attrezzatura.html'
    success_message = 'Attrezzatura modificata correttamente!'
    #success_url = reverse_lazy('human_resources:tabelle_generiche_formazione')
    
    def get_success_url(self):          
        if 'salva_esci' in self.request.POST:
            return reverse_lazy('manutenzioni:dashboard_manutenzioni')
        
        pk_attrezzatura=self.object.pk
        return reverse_lazy('manutenzioni:modifica_attrezzatura', kwargs={'pk':pk_attrezzatura})   
        
            

    def form_valid(self, form):        
        messages.info(self.request, self.success_message) # Compare sul success_url
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):        
        context = super().get_context_data(**kwargs)
        pk_attrezzatura = self.object.pk        
        context['elenco_man_straord'] = ManutenzioneStraordinaria.objects.filter(fk_attrezzatura=pk_attrezzatura) 
        context['elenco_tarature'] = Taratura.objects.filter(fk_attrezzatura=pk_attrezzatura) 
        context['elenco_man_ord'] = ManutenzioneOrdinaria.objects.filter(fk_attrezzatura=pk_attrezzatura) 

        return context



def delete_attrezzatura(request, pk): 
        deleteobject = get_object_or_404(Attrezzatura, pk = pk)                 
        deleteobject.delete()
        url_match = reverse_lazy('manutenzioni:dashboard_manutenzioni')
        return redirect(url_match)


# Manutenzione Ordinaria

class ManutenzioneOrdinariaCreateView(LoginRequiredMixin,CreateView):
    model = ManutenzioneOrdinaria
    form_class = ManutenzioneOrdinariaModelForm
    template_name = 'manutenzioni/manutenzione_ordinaria.html'
    success_message = 'Manutenzione ordinaria aggiunta correttamente!'
    #success_url = reverse_lazy('human_resources:human_resources')

    def get_success_url(self):        
        fk_attrezzatura = self.object.fk_attrezzatura.pk
        return reverse_lazy('manutenzioni:modifica_attrezzatura', kwargs={'pk':fk_attrezzatura})
        
    
    def form_valid(self, form):        
        messages.info(self.request, self.success_message) # Compare sul success_url
        return super().form_valid(form)
    
    def get_initial(self):
        for key, value in self.kwargs.items():
            print(f"Chiave: {key}, Valore: {value}")
        fk_attrezzatura = self.kwargs["fk_attrezzatura"]
        created_by = self.request.user
        return {
            'created_by': created_by,
            'fk_attrezzatura': fk_attrezzatura
        }

class ManutenzioneOrdinariaUpdateView(LoginRequiredMixin, UpdateView):
    model = ManutenzioneOrdinaria
    form_class = ManutenzioneOrdinariaModelForm
    template_name = 'manutenzioni/manutenzione_ordinaria.html'
    success_message = 'Manutenzione modificata correttamente!'
    #success_url = reverse_lazy('human_resources:tabelle_generiche_formazione')
    
    def get_success_url(self):        
        fk_attrezzatura = self.object.fk_attrezzatura.pk
        return reverse_lazy('manutenzioni:modifica_attrezzatura', kwargs={'pk':fk_attrezzatura})
            

    def form_valid(self, form):        
        messages.info(self.request, self.success_message) # Compare sul success_url
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):        
        context = super().get_context_data(**kwargs)
        #pk_attrezzatura = self.object.pk        
        #context['elenco_man_straord'] = ManutenzioneStraordinaria.objects.filter(fk_attrezzatura=pk_attrezzatura) 
        #context['elenco_tarature'] = Taratura.objects.filter(fk_attrezzatura=pk_attrezzatura) 
        #context['elenco_man_ord'] = ManutenzioneOrdinaria.objects.filter(fk_attrezzatura=pk_attrezzatura) 

        return context



def delete_manutenzione_ordinaria(request, pk): 
        deleteobject = get_object_or_404(ManutenzioneOrdinaria, pk = pk)                 
        fk_attrezzatura = deleteobject.fk_attrezzatura.pk
        deleteobject.delete()
        url_match = reverse_lazy('manutenzioni:modifica_attrezzatura', kwargs={'pk':fk_attrezzatura})
        return redirect(url_match)


# Manutenzione Straordinaria

class ManutenzioneStraordinariaCreateView(LoginRequiredMixin,CreateView):
    model = ManutenzioneStraordinaria
    form_class = ManutenzioneStraordinariaModelForm
    template_name = 'manutenzioni/manutenzione_straordinaria.html'
    success_message = 'Manutenzione ordinaria aggiunta correttamente!'
    #success_url = reverse_lazy('human_resources:human_resources')

    def get_success_url(self):        
        fk_attrezzatura = self.object.fk_attrezzatura.pk
        return reverse_lazy('manutenzioni:modifica_attrezzatura', kwargs={'pk':fk_attrezzatura})
        
    
    def form_valid(self, form):        
        messages.info(self.request, self.success_message) # Compare sul success_url
        return super().form_valid(form)
    
    def get_initial(self):
        for key, value in self.kwargs.items():
            print(f"Chiave: {key}, Valore: {value}")
        fk_attrezzatura = self.kwargs["fk_attrezzatura"]
        created_by = self.request.user
        return {
            'created_by': created_by,
            'fk_attrezzatura': fk_attrezzatura
        }

class ManutenzioneStraordinariaUpdateView(LoginRequiredMixin, UpdateView):
    model = ManutenzioneStraordinaria
    form_class = ManutenzioneStraordinariaModelForm
    template_name = 'manutenzioni/manutenzione_straordinaria.html'
    success_message = 'Manutenzione modificata correttamente!'
    #success_url = reverse_lazy('human_resources:tabelle_generiche_formazione')
    
    def get_success_url(self):        
        fk_attrezzatura = self.object.fk_attrezzatura.pk
        return reverse_lazy('manutenzioni:modifica_attrezzatura', kwargs={'pk':fk_attrezzatura})
            

    def form_valid(self, form):        
        messages.info(self.request, self.success_message) # Compare sul success_url
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):        
        context = super().get_context_data(**kwargs)
        #pk_attrezzatura = self.object.pk        
        #context['elenco_man_straord'] = ManutenzioneStraordinaria.objects.filter(fk_attrezzatura=pk_attrezzatura) 
        #context['elenco_tarature'] = Taratura.objects.filter(fk_attrezzatura=pk_attrezzatura) 
        #context['elenco_man_ord'] = ManutenzioneOrdinaria.objects.filter(fk_attrezzatura=pk_attrezzatura) 

        return context



def delete_manutenzione_straordinaria(request, pk): 
        deleteobject = get_object_or_404(ManutenzioneStraordinaria, pk = pk)                 
        fk_attrezzatura = deleteobject.fk_attrezzatura.pk
        deleteobject.delete()
        url_match = reverse_lazy('manutenzioni:modifica_attrezzatura', kwargs={'pk':fk_attrezzatura})
        return redirect(url_match)


# Taratura

class TaraturaCreateView(LoginRequiredMixin,CreateView):
    model = Taratura
    form_class = TaraturaModelForm
    template_name = 'manutenzioni/taratura.html'
    success_message = 'Manutenzione ordinaria aggiunta correttamente!'
    #success_url = reverse_lazy('human_resources:human_resources')

    def get_success_url(self):        
        fk_attrezzatura = self.object.fk_attrezzatura.pk
        return reverse_lazy('manutenzioni:modifica_attrezzatura', kwargs={'pk':fk_attrezzatura})
        
    
    def form_valid(self, form):        
        messages.info(self.request, self.success_message) # Compare sul success_url
        return super().form_valid(form)
    
    def get_initial(self):        
        fk_attrezzatura = self.kwargs["fk_attrezzatura"]
        created_by = self.request.user
        return {
            'created_by': created_by,
            'fk_attrezzatura': fk_attrezzatura
        }

class TaraturaUpdateView(LoginRequiredMixin, UpdateView):
    model = Taratura
    form_class = TaraturaModelForm
    template_name = 'manutenzioni/taratura.html'
    success_message = 'Manutenzione modificata correttamente!'
    #success_url = reverse_lazy('human_resources:tabelle_generiche_formazione')
    
    def get_success_url(self):        
        fk_attrezzatura = self.object.fk_attrezzatura.pk
        return reverse_lazy('manutenzioni:modifica_attrezzatura', kwargs={'pk':fk_attrezzatura})
            

    def form_valid(self, form):        
        messages.info(self.request, self.success_message) # Compare sul success_url
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):        
        context = super().get_context_data(**kwargs)
        #pk_attrezzatura = self.object.pk        
        #context['elenco_man_straord'] = ManutenzioneStraordinaria.objects.filter(fk_attrezzatura=pk_attrezzatura) 
        #context['elenco_tarature'] = Taratura.objects.filter(fk_attrezzatura=pk_attrezzatura) 
        #context['elenco_man_ord'] = ManutenzioneOrdinaria.objects.filter(fk_attrezzatura=pk_attrezzatura) 

        return context



def delete_taratura(request, pk): 
        deleteobject = get_object_or_404(Taratura, pk = pk)                 
        fk_attrezzatura = deleteobject.fk_attrezzatura.pk
        deleteobject.delete()
        url_match = reverse_lazy('manutenzioni:modifica_attrezzatura', kwargs={'pk':fk_attrezzatura})
        return redirect(url_match)