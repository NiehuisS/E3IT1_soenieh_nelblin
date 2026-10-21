from klassen import Gericht, Bestellung

def test_gesamtpreis_mehrere_pizzen():
    pizza = Gericht("Pizza Funghi", 13.00, True)

    bestellung = Bestellung(1002, "offen", {})
    bestellung.hinzufuegen(pizza, 3)

    assert bestellung.gesamtpreis() == 39.00