from zajecia1.zad3.osoba import Osoba


class Pracownik(Osoba):
    def __init__(self, imie: str, nazwisko: str, wiek: int, stanowisko: str, pensja: float):
        super().__init__(imie, nazwisko, wiek)
        self.stanowisko = stanowisko
        self.pensja = pensja

    def info_o_pracy(self):
        return f"Pracuję jako {self.stanowisko}, zarabiam {self.pensja} zł."