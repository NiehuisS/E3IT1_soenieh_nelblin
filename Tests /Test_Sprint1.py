from klassen import Gericht, Kunde, Bestellung 

def test_gesamtpreis_der_bestellung():
    kunde = Kunde("Mina Beispiel", "Beispielstraße 1")
    pizza = Gericht("Pizza Margherita", 12.00, True)
    getraenk = Gericht("Apfelschorle", 3.00, True)
    bestellung = Bestellung(1001, kunde, {})
    bestellung.hinzufuegen(pizza, 2)
    bestellung.hinzufuegen(getraenk, 1)
    assert bestellung.gesamtpreis() == 27.00
