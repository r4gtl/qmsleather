import django_filters
from django import forms
from .models import ProdottoChimico, Sostanza, SostanzaSVHC
from anagrafiche.models import Fornitore




class ProdottoChimicoFilter(django_filters.FilterSet):
    
    descrizione=django_filters.CharFilter(field_name='descrizione', lookup_expr='icontains', widget=forms.TextInput(attrs={'style': 'width: 90%; margin-left: 5%'}))
    fk_fornitore = django_filters.ModelChoiceFilter(
        field_name='fk_fornitore',
        queryset=Fornitore.objects.filter(categoria=Fornitore.PRODOTTI_CHIMICI),
        label='Fornitore'
    )
    
    class Meta:
        model = ProdottoChimico
        fields = ['descrizione', 'fk_fornitore']



class SostanzaFilter(django_filters.FilterSet):
    
    num_cas=django_filters.CharFilter(field_name='num_cas', lookup_expr='icontains', widget=forms.TextInput(attrs={'style': 'width: 90%; margin-left: 5%'}))
    num_ec=django_filters.CharFilter(field_name='num_cas', lookup_expr='icontains', widget=forms.TextInput(attrs={'style': 'width: 90%; margin-left: 5%'}))
    
    class Meta:
        model = Sostanza
        fields = ['num_cas', 'num_ec']



class SostanzaSVHCFilter(django_filters.FilterSet):
    
    num_cas_svhc=django_filters.CharFilter(field_name='num_cas', lookup_expr='icontains', widget=forms.TextInput(attrs={'style': 'width: 90%; margin-left: 5%'}))
    num_ec_svhc=django_filters.CharFilter(field_name='num_cas', lookup_expr='icontains', widget=forms.TextInput(attrs={'style': 'width: 90%; margin-left: 5%'}))
    
    class Meta:
        model = SostanzaSVHC
        fields = ['num_cas', 'num_ec']