from kalkulator_procent import KalkulatorProcent


class Kalkulator():
    def __init__(self):
        self.kalkulatory_procentow: list = []
        self.ubezpieczenie_spoleczne: float = 0.0
        self.ubezpieczenie_zdrowotne: float = 0.0
        self.suma_wszystkich_przychodow: float = 0.0
        self.odliczenia: float = 0.0
        self.podatek: float = 0.0

    def dodaj_kalkulator_procent(self, koszta: list, procent: float) -> None:
        self.kalkulatory_procentow.append(KalkulatorProcent(koszta, procent))

    def dodaj_ubezpieczenie_spoleczne(self, kwota: float):
        self.ubezpieczenie_spoleczne = kwota

    def dodaj_ubezpieczenie_zdrowotne(self, kwota: float):
        self.ubezpieczenie_zdrowotne = kwota

    def licz_przychody_wg_stawek(self):
        for kalkulator in self.kalkulatory_procentow:
            print(f'{kalkulator.procent * 100}%: {kalkulator.suma_przychodow} zl')
            self.suma_wszystkich_przychodow += kalkulator.suma_przychodow
        print(f'Suma przychodu: {self.suma_wszystkich_przychodow} zl')

    def licz_struktura_przychodow(self):
        for kalkulator in self.kalkulatory_procentow:
            kalkulator.set_struktura_przychodu(self.suma_wszystkich_przychodow)
            print(
                f'{kalkulator.procent * 100}%: {kalkulator.suma_przychodow} / {self.suma_wszystkich_przychodow} = {int(kalkulator.struktura_przychodu * 100)} %')

    def licz_odliczenia(self):
        self.odliczenia = round(self.ubezpieczenie_spoleczne +
                                (0.5 * self.ubezpieczenie_zdrowotne), 2)

    def licz_rozliczenie_odliczen(self):
        for kalkulator in self.kalkulatory_procentow:
            kalkulator.set_odliczenie(self.odliczenia)
            print(f'{kalkulator.procent * 100}%: {kalkulator.struktura_przychodu * 100} % * {self.odliczenia} = {kalkulator.odliczenie} zl')

    def licz_podstawa_opodatkowania(self):
        for kalkulator in self.kalkulatory_procentow:
            kalkulator.set_podstawa_opodatkowania()
            print(
                f'{kalkulator.procent * 100}%: {kalkulator.suma_przychodow} - {kalkulator.odliczenie} = {kalkulator.podstawa_opodatkowania} zl')

    def licz_podatek(self):
        for kalkulator in self.kalkulatory_procentow:
            kalkulator.set_podatek()
            print(
                f'{kalkulator.procent * 100}% * {kalkulator.podstawa_opodatkowania} = {kalkulator.podatek} zl')

    def licz_suma_podatku(self):
        suma: float = 0.0
        for kalkulator in self.kalkulatory_procentow:
            suma += kalkulator.podatek
        print(f'Suma podatku: {round(suma, 2)} zl')
