from klassen import Kunde, Pizza, Pasta, Getraenk, Bestellung

def test_bestellung_mehrere_gerichte_verwalten(): 
    kunde = Kunde("Max Mustermann", "Musterstraße 5") 
    pizza = Pizza("Margherita", 12.00, "klein") 
    pizzaF = Pizza("Funghi", 13.00, "mittel")
    pasta = Pasta("Rigatoni Bolognese", 11.00, True)
    getraenk = Getraenk("Coca Cola", 4.00, 0.4) 
    bestellung = Bestellung(1003, kunde, {}) 
    bestellung.hinzufuegen(pizza, 2)
    bestellung.hinzufuegen(pizzaF, 1)
    bestellung.hinzufuegen(pasta, 1)
    bestellung.hinzufuegen(getraenk, 3) 
    assert bestellung.gesamtpreis() == pytest.approx(56.30)
    assert pizza.get_preis() == 12.00 
    assert pizza.get_groesse() == "klein"
    assert pizzaF.get_preis() == 13.00
    assert pizzaF.get_groesse() == "mittel"
    assert pasta.get_preis() == 11.00
    assert pasta.get_cheese() == True
    assert getraenk.get_preis() == 4.00
    assert getraenk.get_volumen() == 0.4

    assert pizzaF.get_groesse() == "mittel"
    assert pasta.get_preis() == 11.00
    assert pasta.get_cheese() == True
    assert getraenk.get_preis() == 4.00
    assert getraenk.get_volumen() == 0.4
