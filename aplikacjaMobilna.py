import json


class AplikacjaMobilna:
    liczba_pobran = 0

    #Konstruktor
    def __init__(self, nazwa, wersja):
        self.nazwa = nazwa
        self.wersja = wersja

    def nowe_pobranie(self):
        AplikacjaMobilna.liczba_pobran += 1

    # Metoda klasy w Pythonie to metoda, która działa na poziomie
    # klasy, a nie konkretnej instancji obiektu.
    # Jest oznaczona dekoratorem @classmethod i jako pierwszy
    # argument przyjmuje cls, który odnosi się do samej klasy
    @classmethod
    def ile_pobran(cls):
        return cls.liczba_pobran

    @classmethod
    def z_json(cls, nazwa_pliku):
        with open(nazwa_pliku, "r", encoding="utf-8") as plik:
            dane = json.load(plik)
        return cls(dane["nazwa"], dane["wersja"])


aplikacja = AplikacjaMobilna.z_json("app.json")
aplikacja.nowe_pobranie()
print(f"Aplikacja: {aplikacja.nazwa}, Wersja: {aplikacja.wersja}")
print(f"Łączna liczba pobrań: {AplikacjaMobilna.ile_pobran()}")
