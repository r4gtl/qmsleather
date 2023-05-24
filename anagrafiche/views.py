from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView
from django_filters.views import FilterView
from .models import Fornitore, Facility
from .forms import FormFornitore, FormFacility
from .filters import FornitoreFilter

# Create your views here.

def home_fornitori(request): 
    fornitori = Fornitore.objects.all()
    filterset_class = FornitoreFilter
    context = {
        'fornitori': filterset_class,
        'filterset': filterset_class
    }
    return render(request, 'anagrafiche/home_fornitori.html', context)

def vedi_fornitore(request, pk):
    fornitore = get_object_or_404(Fornitore, pk=pk)
    context = {'fornitore': fornitore}
    return render(request, "anagrafiche/fornitore.html", context)



def aggiungi_fornitore(request, pk):
    fornitore = get_object_or_404(Fornitore, pk=pk)
    if request.method == "POST":
        form = FormFornitore(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.instance.fornitore = fornitore
        else:
            form = FormFornitore()
        context = {'fornitore': fornitore, 'form': form}
        return render(request, "anagrafiche/fornitore.html", context)

class CreateSupplier(CreateView):
    model = Fornitore
    fields = "__all__"
    
    template_name = "anagrafiche/fornitore.html"
    

class ListaFornitoriView(FilterView):

        model = Fornitore
        context_object_name = 'initial_fornitori'
        template_name = "anagrafiche/home_fornitori.html"
        filterset_class = FornitoreFilter
        paginate_by = 30
        # ordering = ['-iddettordine']
        
def aggiungi_facility_details(request, pk):
    facility = get_object_or_404(Facility, pk=pk)
    if request.method == "POST":
        form = FormFacility(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.instance.facility = facility
        else:
            form = FormFacility()
        context = {'facility': facility, 'form': form}
        
        return render(request, "anagrafiche/facility.html", context)
    
    
class FacilityCreateView(CreateView):
    template_name = 'anagrafiche/facility.html'
    form_class = FormFacility
    
class FacilityUpdateView(UpdateView):
    template_name = 'anagrafiche/facility.html'
    form_class = FormFacility

    
    