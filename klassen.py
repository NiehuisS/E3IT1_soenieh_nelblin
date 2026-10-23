import sys
import os

sys.path.append(os.path.abspath("src"))

class Kunde:
    def __init__(self, name:str, adresse:str):
        self.name = name
        self.adresse = adresse


class Gericht:
    def __init__(self, name:str, preis:float, vegetarisch:bool = False):
        self.name = name
        self.__preis = preis
        self.vegetarisch = vegetarisch

    def get_preis(self):
        return self.__preis

class Bestellung:
    def __init__(self, bestellnummer: int, kunde_oder_status, gericht_mengen=None):
        self.bestellnummer = bestellnummer

        if isinstance(kunde_oder_status, Kunde):
            self.kunde = kunde_oder_status
            self.status = "offen"
        else:
            self.kunde = None
            self.status = kunde_oder_status

        self.gericht_mengen: list = []

    def hinzufuegen(self, gericht: Gericht, menge: int):
        for index, (vorhandenes_gericht, vorhandene_menge) in enumerate(self.gericht_mengen):
            if vorhandenes_gericht == gericht:
                self.gericht_mengen[index] = (gericht, vorhandene_menge + menge)
                return
        
        self.gericht_mengen.append((gericht, menge))
        
    def gesamtpreis(self) -> float:
        gesamt = 0

        for gericht, menge in self.gericht_mengen:
            gesamt += gericht.get_preis() * menge
        
        return gesamt

class Pizza(Gericht):
    def __init__(self, name: str, preis: float, groesse: str):
        super().__init__(name, preis)
        self.__groesse = groesse

    def get_groesse(self):
        return self.__groesse

class Getraenk(Gericht):
    def __init__(self, name: str, preis: float, volumen: float):
        super().__init__(name, preis)
        self.__volumen = volumen

    def get_volumen(self):
        return self.__volumen

class Pasta(Gericht):
    def __init__(self, name: str, preis: float, cheese: bool):
        super().__init__(name, preis)
        self.__cheese = cheese

    def get_cheese(self):
        return self.__cheese
