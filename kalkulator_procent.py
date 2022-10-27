class KalkulatorProcent():
    def __init__(self, koszta: list, procent: float) -> None:
        self.przychody: float = koszta
        self.procent: float = procent
        self.suma_przychodow: float = self.set_suma_przychodow()
        self.struktura_przychodu: float = 0.0
        self.odliczenie: float = 0.0
        self.podstawa_opodatkowania: float = 0.0
        self.podatek: float = 0.0

    def set_suma_przychodow(self) -> float:
        suma = 0
        for przychod in self.przychody:
            suma += przychod
        return suma

    def set_struktura_przychodu(self, suma_wszystkich_kosztow: float) -> None:
        self.struktura_przychodu = round(
            self.suma_przychodow / suma_wszystkich_kosztow, 2)

    def set_odliczenie(self, suma_odliczen: float) -> None:
        self.odliczenie = round(self.struktura_przychodu * suma_odliczen, 2)

    def set_podstawa_opodatkowania(self) -> None:
        self.podstawa_opodatkowania = int(
            self.suma_przychodow - self.odliczenie)

    def set_podatek(self) -> None:
        self.podatek = round(self.procent * self.podstawa_opodatkowania, 2)
