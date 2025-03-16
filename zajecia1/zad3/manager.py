from zajecia1.zad3.pracownik import Pracownik


class Manager(Pracownik):
    def __init__(self, imie: str, nazwisko: str, wiek: int, stanowisko: str, pensja: float):
        super().__init__(imie, nazwisko, wiek, stanowisko, pensja)
        self.zespol = []

    def przedstaw_sie(self):
        return f"Jestem {self.imie} {self.nazwisko}, zarządzam zespołem {len(self.zespol)} pracowników."

    def dodaj_do_zespolu(self, pracownik: Pracownik):
        self.zespol.append(pracownik)