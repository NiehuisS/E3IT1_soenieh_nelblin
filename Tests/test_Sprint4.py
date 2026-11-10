from klassen import Gericht, Bestellung, Kunde, Pizza, Getraenk

def test_gerichte_berechnen_unterschiedliche_preise(): 
    kunde = Kunde("Mina Beispiel", "Beispielstraße 1") 
    pizza = Pizza("Margherita", 12.00, "mittel") 
    getraenk = Getraenk("Apfelschorle", 3.00, 0.5) 
    bestellung = Bestellung(1001, kunde) 
    bestellung.hinzufuegen(pizza, 2) 
    bestellung.hinzufuegen(getraenk, 1) 
    assert bestellung.gesamtpreis() == 24.60 
