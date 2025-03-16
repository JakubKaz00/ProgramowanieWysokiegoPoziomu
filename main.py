#Wywolanie aplikacja mobilna
from aplikacjaMobilna import AplikacjaMobilna

aplikacja = AplikacjaMobilna.z_json("app.json")

print(f"Aplikacja: {aplikacja.nazwa}, Wersja: {aplikacja.wersja}")

aplikacja.nowe_pobranie()

print(f"Łączna liczba pobrań: {AplikacjaMobilna.ile_pobran()}")
