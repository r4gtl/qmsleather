from django import forms
from django_countries.widgets import CountrySelectWidget
from django_countries.fields import CountryField
from .models import (Attrezzatura, ManutenzioneStraordinaria, Taratura,
                    ManutenzioneOrdinaria,
                    )

from anagrafiche.models import Fornitore

class AttrezzaturaModelForm(forms.ModelForm):
    class Meta:
        model = Attrezzatura
        fields = '__all__'
        
        widget = {
            
            'codice_attrezzatura': forms.TextInput(attrs={'placeholder': 'Inserisci codice attrezzatura'}),
            'descrizione': forms.TextInput(attrs={'placeholder': 'Inserisci descrizione'}),
            'modello': forms.TextInput(attrs={'placeholder': 'Inserisci modello'}),
            'serie_matricola': forms.TextInput(attrs={'placeholder': 'Inserisci serie/matricola'}),
            'is_taratura': forms.CheckboxInput(),
            'periodo_taratura': forms.TextInput(attrs={'placeholder': 'Inserisci periodo taratura'}),            
            'note': forms.Textarea(attrs={'placeholder': 'Inserisci Annotazioni', 'rows':'3'}),
            'created_by': forms.HiddenInput(),
            'created_at': forms.HiddenInput()
        }
        labels = {
            
            'codice_attrezzatura': 'Codice Attrezzatura',
            'descrizione': 'Descrizione',
            'modello': 'Modello',
            'serie_matricola': 'N. serie/N. Matricola',
            'is_taratura': 'Soggetto a taratura',
            'periodo_taratura': 'Periodi di taratura',
            'note': 'Annotazioni'
        }
        
class ManutenzioneStraordinariaModelForm(forms.ModelForm):
    class Meta:
        model = ManutenzioneStraordinaria
        fields = '__all__'
        fk_fornitore = forms.ModelChoiceField(queryset=Fornitore.objects.all())
        widget = {
            'data_manutenzione': forms.DateInput(format=('%Y-%m-%d'), attrs={'class':'form-control', 'type': 'date'}),
            'descrizione': forms.TextInput(attrs={'placeholder': 'Inserisci descrizione'}),
            'importo': forms.DecimalField(),
            'ore_fermo': forms.DecimalField(),
            'fk_fornitore': forms.Select(attrs={'style':'background_color:#F5F8EC'}),
            'ft_prot': forms.TextInput(attrs={'placeholder': 'Inserisci codice attrezzatura'}),
            'data_fattura': forms.DateInput(format=('%Y-%m-%d'), attrs={'class':'form-control', 'type': 'date'}),            
            'note': forms.Textarea(attrs={'placeholder': 'Inserisci Annotazioni', 'rows':'3'}),
            'fk_attrezzatura': forms.HiddenInput(),
            'created_by': forms.HiddenInput(),
            'created_at': forms.HiddenInput()
        }
        labels = {
            
            'data_manutenzione': 'Data Manutenzione',
            'descrizione': 'Descrizione',
            'importo': 'Importo',
            'ore_fermo': 'Ore Fermo',
            'fk_fornitore': 'Fornitore',
            'ft_prot': 'Fattura Protocollo',
            'data_fattura': 'Data Fattura',
            'note': 'Annotazioni'
        }
        
class TaraturaModelForm(forms.ModelForm):
    class Meta:
        model = Taratura
        fields = '__all__'
        fk_fornitore = forms.ModelChoiceField(queryset=Fornitore.objects.all())
        widget = {
            'data_taratura': forms.DateInput(format=('%Y-%m-%d'), attrs={'class':'form-control', 'type': 'date'}),
            'fk_fornitore': forms.Select(attrs={'style':'background_color:#F5F8EC'}),            
            'documento': forms.FileField(),
            'is_conforme': forms.CheckboxInput(),
            'prossima_scadenza': forms.DateInput(format=('%Y-%m-%d'), attrs={'class':'form-control', 'type': 'date'}),
            'note': forms.Textarea(attrs={'placeholder': 'Inserisci Annotazioni', 'rows':'3'}),
            'fk_attrezzatura': forms.HiddenInput(),
            'created_by': forms.HiddenInput(),
            'created_at': forms.HiddenInput()
        }
        labels = {
            
            'data_taratura': 'Data Taratura',
            'fk_fornitore': 'Fornitore',
            'documento': 'Documento',
            'is_conforme': 'Conforme',
            'prossima_scadenza': 'Prossima Scadenza',
            'note': 'Annotazioni'
        }
        
class ManutenzioneOrdinariaModelForm(forms.ModelForm):
    class Meta:
        model = ManutenzioneOrdinaria
        fields = '__all__'
        fk_fornitore = forms.ModelChoiceField(queryset=Fornitore.objects.all())
        widget = {
            'data_manutenzione': forms.DateInput(format=('%Y-%m-%d'), attrs={'class':'form-control', 'type': 'date'}),
            'descrizione': forms.TextInput(attrs={'placeholder': 'Inserisci descrizione'}),
            'fk_fornitore': forms.Select(attrs={'style':'background_color:#F5F8EC'}),                        
            'is_eseguita': forms.CheckboxInput(),
            'prossima_scadenza': forms.DateInput(format=('%Y-%m-%d'), attrs={'class':'form-control', 'type': 'date'}),
            'note': forms.Textarea(attrs={'placeholder': 'Inserisci Annotazioni', 'rows':'3'}),
            'fk_attrezzatura': forms.HiddenInput(),
            'created_by': forms.HiddenInput(),
            'created_at': forms.HiddenInput()
        }
        labels = {
            
            'data_manutenzione': 'Data Manutanzione',
            'fk_fornitore': 'Fornitore',
            'descrizione': 'Descrizione',
            'is_eseguita': 'Eseguita',
            'prossima_scadenza': 'Prossima Scadenza',
            'note': 'Annotazioni'
        }
        