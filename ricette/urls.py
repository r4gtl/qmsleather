from django.urls import path

from .utils import *
from .views import *

app_name="ricette"

urlpatterns = [
    
    # Home Ricette
    path('', home_ricette, name='home_ricette'),  
    path('ricette_rifinizione/', home_ricette_rifinizione, name='home_ricette_rifinizione'),  
    
    # Tabelle Generiche
    path('tabelle_generiche/', tabelle_generiche, name='tabelle_generiche'), 
    
    
    # Operazione Ricette
    path('aggiungi_operazione/', OperazioneRicetteCreateView.as_view(), name="aggiungi_operazione"), 
    path('modifica_operazione/<int:pk>/', OperazioneRicetteUpdateView.as_view(), name="modifica_operazione"), 
    path('delete_operazione/<int:pk>', delete_operazione, name="delete_operazione"),

    # Ricette Rifinizione
    path('aggiungi_ricetta_rifinizione/', RicettaRifinizioneCreateView.as_view(), name="aggiungi_ricetta_rifinizione"), 
    path('modifica_ricetta_rifinizione/<int:pk>/', RicettaRifinizioneUpdateView.as_view(), name="modifica_ricetta_rifinizione"), 
    path('delete_ricetta_rifinizione/<int:pk>', delete_ricetta_rifinizione, name="delete_ricetta_rifinizione"),

    # Dettaglio Ricette Rifinizione
    path('<int:fk_ricetta_rifinizione>/aggiungi_dettaglio_ricetta_rifinizione/', DettaglioRicettaRifinizioneCreateView.as_view(), name="aggiungi_dettaglio_ricetta_rifinizione"), 
    path('<int:fk_ricetta_rifinizione>/modifica_dettaglio_ricetta_rifinizione/<int:pk>/', DettaglioRicettaRifinizioneUpdateView.as_view(), name="modifica_dettaglio_ricetta_rifinizione"), 
    path('delete_dettaglio_ricetta_rifinizione/<int:pk>', delete_dettaglio_ricetta_rifinizione, name="delete_dettaglio_ricetta_rifinizione"),

    # Numero riga
    path('update_numero_riga/', update_numero_riga, name="update_numero_riga"),
    #path('get_updated_table_data/', get_updated_table_data, name="get_updated_table_data"),
    path('update_row_numbers/', update_row_numbers, name='update_row_numbers'),
    

    
    
]