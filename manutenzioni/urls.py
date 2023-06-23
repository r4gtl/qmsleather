from django.urls import path
from .views import (dashboard_manutenzioni, scadenzario,
                    AttrezzaturaCreateView, AttrezzaturaUpdateView, delete_attrezzatura,
                    ManutenzioneOrdinariaCreateView, ManutenzioneOrdinariaUpdateView, delete_manutenzione_ordinaria,
                    ManutenzioneStraordinariaCreateView, ManutenzioneStraordinariaUpdateView, delete_manutenzione_straordinaria,
                    TaraturaCreateView, TaraturaUpdateView, delete_taratura,
                    )

app_name="manutenzioni"

urlpatterns = [
    
    # Home Manutenzioni
    path('', dashboard_manutenzioni, name='dashboard_manutenzioni'),    
    path('scadenzario/', scadenzario, name='scadenzario'),    

    # Manage Attrezzatura
    path('crea_attrezzatura/', AttrezzaturaCreateView.as_view(), name="crea_attrezzatura"), 
    path('modifica_attrezzatura/<int:pk>/', AttrezzaturaUpdateView.as_view(), name="modifica_attrezzatura"), 
    path('delete_attrezzatura/<int:pk>', delete_attrezzatura, name="delete_attrezzatura"),

    # Manage Manutenzione Ordinaria
    path('<int:fk_attrezzatura>/aggiungi_manutenzione_ordinaria/', ManutenzioneOrdinariaCreateView.as_view(), name="aggiungi_manutenzione_ordinaria"), 
    path('<int:fk_attrezzatura>/modifica_manutenzione_ordinaria/<int:pk>/', ManutenzioneOrdinariaUpdateView.as_view(), name="modifica_manutenzione_ordinaria"), 
    path('delete_manutenzione_ordinaria/<int:pk>', delete_manutenzione_ordinaria, name="delete_manutenzione_ordinaria"),

    # Manage Manutenzione Straordinaria
    path('<int:fk_attrezzatura>/aggiungi_manutenzione_straordinaria/', ManutenzioneStraordinariaCreateView.as_view(), name="aggiungi_manutenzione_straordinaria"), 
    path('<int:fk_attrezzatura>/modifica_manutenzione_straordinaria/<int:pk>/', ManutenzioneStraordinariaUpdateView.as_view(), name="modifica_manutenzione_straordinaria"), 
    path('delete_manutenzione_straordinaria/<int:pk>', delete_manutenzione_straordinaria, name="delete_manutenzione_straordinaria"),

    # Manage Taratura
    path('<int:fk_attrezzatura>/aggiungi_taratura/', TaraturaCreateView.as_view(), name="aggiungi_taratura"), 
    path('<int:fk_attrezzatura>/modifica_taratura/<int:pk>/', TaraturaUpdateView.as_view(), name="modifica_taratura"), 
    path('delete_taratura/<int:pk>', delete_taratura, name="delete_taratura"),

]