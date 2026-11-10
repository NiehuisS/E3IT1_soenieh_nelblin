from klassen import Pizza, Bestellung

def test_gesamtpreis_mehrere_pizzen():
    pizza = Pizza("Pizza Funghi", 13.00, True)

    bestellung = Bestellung(1002, "offen", {})
    bestellung.hinzufuegen(pizza, 3)

    assert bestellung.gesamtpreis() == pytest.approx(35.10)
