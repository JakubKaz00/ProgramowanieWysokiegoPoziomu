from zajecia1.zad5.komunikacja import Komunikacja
from zajecia1.zad5.rozrywka import Rozrywka
from zajecia1.zad5.smartphone import Smartphone
from zajecia1.zad5.telefon import Telefon

telefon = Telefon("Galaxy S22", "Samsung")
komunikacja = Komunikacja()
rozrywka = Rozrywka()
smartphone = Smartphone(telefon, komunikacja, rozrywka)

print(smartphone.telefon)
smartphone.komunikacja.wyslij_wiadomosc("Jakub Kazmierski", "Cześć, co słychać?")
smartphone.rozrywka.odtworz_muzyke("Przykladowy Tytul")
