from cProfile import label
from django import forms
from django_countries.widgets import CountrySelectWidget
from django_countries.fields import CountryField
from .models import (HumanResource, Ward, Role,
                    AreaFormazione, CorsoFormazione,
                    RegistroFormazione, DettaglioRegistroFormazione,
                    )
from anagrafiche.models import Fornitore


class HumanResourceModelForm(forms.ModelForm):
    class Meta:
        model = HumanResource
        fields = '__all__'
        exclude = ['created_at', 'updated_at']
        country = CountryField().formfield()
        
        widget = {
            
            'cognomedipendente': forms.TextInput(attrs={'class': 'form-control'}),
            'nomedipendente': forms.TextInput(attrs={'class': 'form-control'}),
            'country': CountrySelectWidget(),
            'immagine': forms.ImageField(),
            'gender': forms.ChoiceField(),
            'dataassunzione': forms.DateInput(),
            'datadimissioni': forms.DateInput(),
            'fk_mansione': forms.ChoiceField(),
            'fk_reparto': forms.ChoiceField(),
            'qualifica': forms.TextInput(attrs={'class': 'form-control'}),
            'commenti': forms.Textarea(attrs={'class': 'form-control'}),
            
        },
        labels = {
            'cognomedipendente': 'Cognome',
            'nomedipendente': 'Nome',
            'country': 'Nazionalità',
            'immagine': 'Foto',
            'gender': 'Genere',
            'dataassunzione': 'Data Assunzione',
            'datadimissioni': 'Data Dimissioni',
            'fk_mansione': 'Mansione',
            'fk_reparto': 'Reparto',
            'qualifica': 'Qualifica',
            'commenti': 'Commenti',

        }

class WardModelForm(forms.ModelForm):
    class Meta:
        model = Ward
        fields = '__all__'

class RoleModelForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = '__all__'


'''SEZIONE FORMAZIONE'''        
# Area formazione
class AreaFormazioneModelForm(forms.ModelForm):
    class Meta:
        model = AreaFormazione
        fields = '__all__'
        widgets = {
            'descrizione': forms.TextInput(attrs={'placeholder': 'Inserisci Area Formazione'}),            
            'created_by': forms.HiddenInput()
        }
        
        
# Corso Formazione        
class CorsoFormazioneModelForm(forms.ModelForm):
    class Meta:
        model = CorsoFormazione
        fields = '__all__'
        fk_areaformazione = forms.ModelChoiceField(queryset=AreaFormazione.objects.all())
        widgets = {
            'descrizione': forms.TextInput(attrs={'placeholder': 'Inserisci Corso Formazione'}),
            'fk_areaformazione': forms.Select(attrs={'style':'background_color:#F5F8EC'}),
            'created_by': forms.HiddenInput()
        }
        labels = {
            'descrizione': 'Corso di Formazione',
            'fk_areaformazione': 'Area Formazione',
            

        }

# Registro Formazione
class RegistroFormazioneModelForm(forms.ModelForm):
    class Meta:
        model = RegistroFormazione
        fields = '__all__'
        fk_corso = forms.ModelChoiceField(queryset=CorsoFormazione.objects.all())
        fk_fornitore = forms.ModelChoiceField(queryset=Fornitore.objects.all())
        
        widgets = {
            'data_formazione': forms.DateInput(format=('%Y-%m-%d'), attrs={'class':'form-control', 'type': 'date'}),         
            'fk_corso': forms.Select(attrs={'style':'background_color:#F5F8EC'}),
            'fk_fornitore': forms.Select(attrs={'style':'background_color:#F5F8EC'}),
            'ore': forms.NumberInput(attrs={'class': 'form-control'}),
            'note': forms.Textarea(attrs={'placeholder': 'Inserisci Annotazioni', 'rows':'3'}),
            'created_by': forms.HiddenInput()
        }
        labels = {
            'data_formazione': 'Data Formazione',
            'fk_corso': 'Corso/Attività',
            'fk_fornitore': 'Ente che ha fornito il servizio',
            'ore': 'Ore totali di formazione',
            'note': 'Annotazioni'
        }
        
# Dettaglio Registro Formazione
class DettaglioRegistroFormazioneModelForm(forms.ModelForm):
    class Meta:
        model = DettaglioRegistroFormazione
        fields = '__all__'
        fk_hr = forms.ModelChoiceField(queryset=HumanResource.objects.all())
        widgets = {
            'fk_registro_formazione': forms.HiddenInput(),            
            'fk_hr': forms.Select(attrs={'style':'background_color:#F5F8EC'}),
            'efficace': forms.CheckboxInput(),
            'note': forms.Textarea(attrs={'placeholder': 'Inserisci Annotazioni'}),
            
        }
        labels = {
            'fk_hr': 'Operatore',
            'certificato': 'Certificato',
            'presenza': 'Presenza',
            'efficace': 'Efficace',
            'note': 'Annotazioni'
        }
        