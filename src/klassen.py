import sys
import os
from abc import ABC, abstractmethod
 
sys.path.append(os.path.abspath("src"))
 
class Kunde:
    def __init__(self, name:str, adresse:str):
        self.__name = name
        self.__adresse = adresse

    def get_name(self):
        return self.__name

    def get_adresse(self):
        return self.__adresse

 
class Gericht(ABC):
    def __init__(self, name:str, preis:float, vegetarisch:bool = False):
        
        if preis < 0:
            raise ValueError("Der Preis darf nicht negativ sein.")
        
        self.__name = name
        self.__preis = preis
        self.__vegetarisch = vegetarisch

    def get_name(self):
        return self.__name
 
    def get_preis(self):
        return self.__preis

    def get_vegetarisch(self):
        return self.__vegetarisch

    @abstractmethod
    def berechne_preis(self) -> float:
        pass
 
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

    def abschliessen(self):
        self.__status = "abgeschlossen"

    def get_bestellnummer(self):
        return self.__bestellnummer

    def get_kunde(self):
        return self.__kunde

    def get_status(self):
        return self.__status

    def get_gerichte(self):
        return list(self.__gericht_mengen)
 
    def hinzufuegen(self, gericht: Gericht, menge: int):
        if self.__status in ("abgeschlossen", "ausgeliefert"):
            raise RuntimeError("Die Bestellung darf nicht mehr verändert werden.")

        if menge <= 0:
            raise ValueError("Die Bestellmenge muss größer als 0 sein.")
        
        for index, (vorhandenes_gericht, vorhandene_menge) in enumerate(self.__gericht_mengen):
            if vorhandenes_gericht == gericht:
                self.__gericht_mengen[index] = (gericht, vorhandene_menge + menge)
                return
        
        self.__gericht_mengen.append((gericht, menge))
        
    def gesamtpreis(self) -> float:
        gesamt = 0
 
        for gericht, menge in self.__gericht_mengen:
            gesamt += gericht.berechne_preis() * menge
        
        return gesamt
 
class Pizza(Gericht):
    def __init__(self, name: str, preis: float, groesse: str):
        super().__init__(name, preis)
        self.__groesse = groesse
 
    def get_groesse(self):
        return self.__groesse

    def berechne_preis(self) -> float:
            return self.get_preis() * 0.90
 
class Getraenk(Gericht):
    def __init__(self, name: str, preis: float, volumen: float):
        super().__init__(name, preis)
        self.__volumen = volumen
 
    def get_volumen(self):
        return self.__volumen

    def berechne_preis(self) -> float:
        return self.get_preis()
 
class Pasta(Gericht):
    def __init__(self, name: str, preis: float, cheese: bool):
        super().__init__(name, preis)
        self.__cheese = cheese
 
    def get_cheese(self):
        return self.__cheese

    def berechne_preis(self):
        return self.get_preis()
 
def erstelle_restaurant_bestellung():
    kunde = Kunde("Max", "Musterstraße 1")
    bestellung = Bestellung(1, kunde)

    pizza = Pizza("Margherita", 12.00, "mittel")
    bestellung.hinzufuegen(pizza, 1)

    return bestellung
