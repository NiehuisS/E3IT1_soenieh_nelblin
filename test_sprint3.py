from klassen import Gericht, Bestellung, Kunde, Pizza, Getraenk

def test_unterschiedliche_gerichtarten():
    kunde = Kunde("Mina Beispiel", "Beispielstraße 1")
    pizza = Pizza("Margherita", 12.00, "mittel")
    getraenk = Getraenk("Apfelschorle", 3.00, 0.5)
    bestellung = Bestellung(1001, kunde)
    bestellung.hinzufuegen(pizza, 2)
    bestellung.hinzufuegen(getraenk, 1)
    assert pizza.get_preis() == 12.00
    assert pizza.get_groesse() == "mittel"
    assert getraenk.get_preis() == 3.00
    assert getraenk.get_volumen() == 0.5
    assert bestellung.gesamtpreis() == 27.00