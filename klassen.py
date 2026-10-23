import sys
import os
 
sys.path.append(os.path.abspath("src"))
 
class Kunde:
    def __init__(self, name:str, adresse:str):
        self.__name = name
        self.__adresse = adresse

    def get_name(self):
        return self.__name

    def get_adresse(self):
        return self.__adresse

 
class Gericht:
    def __init__(self, name:str, preis:float, vegetarisch:bool = False):
        self.__name = name
        self.__preis = preis
        self.__vegetarisch = vegetarisch

    def get_name(self):
        return self.__name
 
    def get_preis(self):
        return self.__preis

    def get_vegetarisch(self):
        return self.__vegetarisch
 
class Bestellung:
    def __init__(self, bestellnummer: int, status, gericht_mengen=None):
        self.__bestellnummer = bestellnummer
 
        if isinstance(status, Kunde):
            self.__kunde = status
            self.__status = "offen"
        else:
            self.__kunde = None
            self.__status = status
 
        self.__gericht_mengen: list = []
        if gericht_mengen:
            self.__gericht_mengen = list(gericht_mengen)

    def get_bestellnummer(self):
        return self.__bestellnummer

    def get_kunde(self):
        return self.__kunde

    def get_status(self):
        return self.__status

    def get_gerichte(self):
        return list(self.__gericht_mengen)
 
    def hinzufuegen(self, gericht: Gericht, menge: int):
        for index, (vorhandenes_gericht, vorhandene_menge) in enumerate(self.__gericht_mengen):
            if vorhandenes_gericht == gericht:
                self.__gericht_mengen[index] = (gericht, vorhandene_menge + menge)
                return
        
        self.__gericht_mengen.append((gericht, menge))
        
    def gesamtpreis(self) -> float:
        gesamt = 0
 
        for gericht, menge in self.__gericht_mengen:
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
 
