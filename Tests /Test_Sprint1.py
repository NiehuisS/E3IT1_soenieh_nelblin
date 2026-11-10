from klassen import Pizza, Getraenk, Kunde, Bestellung 

def test_gesamtpreis_der_bestellung():
    kunde = Kunde("Mina Beispiel", "Beispielstraße 1")
    pizza = Pizza("Pizza Margherita", 12.00, True)
    getraenk = Getraenk("Apfelschorle", 3.00, True)
    bestellung = Bestellung(1001, kunde, {})
    bestellung.hinzufuegen(pizza, 2)
    bestellung.hinzufuegen(getraenk, 1)
    assert bestellung.gesamtpreis() == pytest.approx(24.60)
