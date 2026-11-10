from klassen import Pizza, Pasta, Bestellung, Kunde

def test_bestellung_berechnet_gesamtpreis_mit_unterschiedlichen_mengen():
    kunde = Kunde("Max Mustermann", "Musterstraße 5")
    pizza = Pizza("Pizza Margherita", 12.00, True)
    pasta = Pasta("Pasta", 10.00, True)

    bestellung = Bestellung(1002, kunde, {})

    bestellung.hinzufuegen(pizza, 3)
    bestellung.hinzufuegen(pasta, 2)

    assert bestellung.gesamtpreis() == pytest.approx(52.40)
    assert pizza.get_preis() == 12.00
    assert pasta.get_preis() == 10.00
