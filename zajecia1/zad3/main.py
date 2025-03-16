from zajecia1.zad3.manager import Manager
from zajecia1.zad3.pracownik import Pracownik

manager = Manager("Anna", "Kowalska", 40, "Dyrektor", 15000)
pracownik1 = Pracownik("Jan", "Nowak", 30, "Programista", 8000)
pracownik2 = Pracownik("Ewa", "Wiśniewska", 28, "Analityk", 7500)

manager.dodaj_do_zespolu(pracownik1)
manager.dodaj_do_zespolu(pracownik2)

test_output = [
    manager.przedstaw_sie(),
    manager.info_o_pracy(),
    pracownik1.przedstaw_sie(),
    pracownik1.info_o_pracy(),
    pracownik2.przedstaw_sie(),
    pracownik2.info_o_pracy()
]

for output in test_output:
    print(output)
