class Kunde:
    def __init__(self, name:str, adresse:str):
        self.name = name
        self.adresse = adresse


class Gericht:
    def __init__(self, name:str, preis:float, vegetarisch:bool):
        self.name = name
        self.preis = preis
        self.vegetarisch = vegetarisch


class Bestellung:
    def __init__(self, bestellnummer:int, status:str, gericht_mengen:dict):
        self.bestellnummer = bestellnummer
        self.status = status
        self.gericht_mengen = gericht_mengen

        self.gericht_mengen: dict[Gericht, int] = {}

    def hinzufuegen(self, gericht:Gericht, menge:int):
        self.gericht_mengen[gericht] = menge
    
    def gesamtpreis(self) -> float:
        gesamt = 0

        for gericht, menge in self.gericht_mengen.items():
            gesamt += gericht.preis * menge
        
        return gesamt