import pytest
import os
import sys

sys.path.insert(0, os.path.abspath("src"))

from klassen import (Bestellung, Kunde, Gericht, Pizza, Getraenk, erstelle_restaurant_bestellung)

def test_negativer_gerichtspreis_wird_abgelehnt(): 
    with pytest.raises(ValueError): 
        Pizza("Margherita", -1.00, "mittel") 

def test_bestellmenge_muss_groesser_null_sein(): 
    bestellung = erstelle_restaurant_bestellung() 
    pizza = Pizza("Margherita", 12.00, "mittel") 
    
    with pytest.raises(ValueError): 
        bestellung.hinzufuegen(pizza, 0) 

def test_abgeschlossene_bestellung_kann_nicht_mehr_veraendert_werden(): 
    bestellung = erstelle_restaurant_bestellung() 
    bestellung.abschliessen() 
    getraenk = Getraenk("Apfelschorle", 3.00, 0.5) 
 
    with pytest.raises(RuntimeError): 
        bestellung.hinzufuegen(getraenk, 1) 

def test_abstrakte_gerichtklasse_kann_nicht_erzeugt_werden(): 
    with pytest.raises(TypeError): 
        Gericht() 
