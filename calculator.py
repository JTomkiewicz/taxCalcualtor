class KalkulatorProcent():
    def __init__(self, koszta, procent):
        self.przychody = koszta
        self.procent = procent
        self.suma_przychodow = self.set_suma_przychodow()
        self.struktura_przychodu = 0
        self.odliczenie = 0
        self.podstawa_opodatkowania = 0

    def set_suma_przychodow(self):
        suma = 0
        for przychod in self.przychody:
            suma += przychod
        return suma

    def set_struktura_przychodu(self, suma_wszystkich_kosztow):
        self.struktura_przychodu = self.suma_przychodow / suma_wszystkich_kosztow

    def set_odliczenie(self, suma_odliczen):
        self.odliczenie = self.struktura_przychodu * suma_odliczen

    def set_podstawa_opodatkowania(self):
        self.podstawa_opodatkowania = int(self.procent - self.odliczenie)

    def set_podatek(self):
        self.podatek = self.procent * self.podstawa_opodatkowania


class Kalkulator():
    def __init__(self):
        self.kalkulatory_procentow = []
        self.ubezpieczenie_spoleczne = 0
        self.ubezpieczenie_zdrowotne = 0
        self.suma_wszystkich_przychodow = 0
        self.odliczenia = 0
        self.podatek = 0

    def dodaj_kalkulator_procent(self, koszta, procent):
        self.kalkulatory_procentow.append(KalkulatorProcent(koszta, procent))

    def licz_przychody_wg_stawek(self):
        for kalkulator in self.kalkulatory_procentow:
            print(f'{kalkulator.procent * 100}%: {kalkulator.suma_przychodow} zl')
            self.suma_wszystkich_przychodow += kalkulator.suma_przychodow
        print(f'Suma przychodu: {self.suma_wszystkich_przychodow} zl')

    def licz_struktura_przychodow(self):
        for kalkulator in self.kalkulatory_procentow:
            kalkulator.set_struktura_przychodu(self.suma_wszystkich_przychodow)
            print(f'{kalkulator.procent * 100}%: {kalkulator.struktura_przychodu}%')

    def licz_odliczenia(self):
        self.odliczenia = self.ubezpieczenie_spoleczne + \
            (0.5 * self.ubezpieczenie_zdrowotne)

    def licz_rozliczenie_odliczen(self):
        for kalkulator in self.kalkulatory_procentow:
            kalkulator.set_odliczenie(self.odliczenia)
            print(f'{kalkulator.procent * 100}%: {kalkulator.odliczenie} zl')

    def licz_podstawa_opodatkowania(self):
        for kalkulator in self.kalkulatory_procentow:
            kalkulator.set_podstawa_opodatkowania()
            print(
                f'{kalkulator.procent * 100}%: {kalkulator.podstawa_opodatkowania} zl')

    def licz_podatek(self):
        for kalkulator in self.kalkulatory_procentow:
            kalkulator.set_podatek()
            print(f'{kalkulator.procent * 100}%: {kalkulator.podatek} zl')

    def licz_suma_podatku(self):
        suma = 0
        for kalkulator in self.kalkulatory_procentow:
            suma += kalkulator.podatek
        print(f'Suma podatku: {suma} zl')
