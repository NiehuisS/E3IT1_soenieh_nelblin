import sys 
import os

from klassen import Kunde, Gericht, Pizza, Getraenk, Bestellung

def test_bestellung_sprint4():
    kunde = Kunde("Max Muster", "Musterstrasse 5")

    pizza = Pizza("Salami", 10.00, "groß")
    getraenk = Getraenk("Cola", 2.50, 0.5)
    bestellung = Bestellung(1002, kunde, {})
    bestellung.hinzufuegen(pizza, 2)
    bestellung.hinzufuegen(getraenk, 2)
    assert bestellung.gesamtpreis() == 23.00
