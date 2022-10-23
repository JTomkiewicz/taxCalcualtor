class Calculator():
    def __init__(self, array, percent):
        self.arr = array
        self.percent = percent
        self.sum = self.calculate_sum()
        self.przychod = 0
        self.odliczenie = 0
        self.podstawa_opodatakowania = 0

    def calculate_sum(self):
        sum = 0
        for item in self.arr:
            sum += item
        return sum

    def get_sum(self):
        return self.sum

    def set_przychod(self, total_sum):
        self.przychod = self.sum / total_sum

    def get_przychod(self):
        return self.przychod

    def set_odliczenie(self, suma_odliczen):
        self.odliczenie = self.przychod * suma_odliczen

    def get_odliczenie(self):
        return self.odliczenie

    def set_podstawa_opodatkowania(self):
        self.podstawa_opodatakowania = int(self.percent - self.odliczenie)

    def get_podstawa_opodatkowania(self):
        return self.podstawa_opodatakowania

    def set_podatek(self):
        self.podatek = self.percent * self.podstawa_opodatakowania

    def get_podatek(self):
        return self.podatek


def main():
    c3 = Calculator([2000, 200, 185, 1100, 2000, 210, - 120, 20], 0.03)
    c5_5 = Calculator([500, 1000, 500], 0.055)
    c8_5 = Calculator([100, 250, 200, -50], 0.085)
    ubezpiecznie_spoleczne = 500
    ubezpiecznie_zdrowotne = 150

    print('--- Przychody wg stawek ---')
    print('Suma of 3%: ', c3.get_sum())
    print('Suma of 5.5%: ', c5_5.get_sum())
    print('Suma of 8.5%: ', c8_5.get_sum())

    total_sum = c3.get_sum() + c5_5.get_sum() + c8_5.get_sum()

    print(f'Razem przychody: {total_sum}')

    print('--- Struktura przychodow ---')

    c3.set_przychod(total_sum)
    c5_5.set_przychod(total_sum)
    c8_5.set_przychod(total_sum)

    print('3%: ', c3.get_przychod())
    print('5.5%: ', c5_5.get_przychod())
    print('8.5%: ', c8_5.get_przychod())

    print('--- Rozliczenie odliczen ---')

    odliczenia = ubezpiecznie_spoleczne + (0.5 * ubezpiecznie_zdrowotne)

    c3.set_odliczenie(odliczenia)
    c5_5.set_odliczenie(odliczenia)
    c8_5.set_odliczenie(odliczenia)

    print(f'Odliczenie 3%: {c3.get_odliczenie()}')
    print(f'Odliczenie 5.5%: {c5_5.get_odliczenie()}')
    print(f'Odliczenie 8.5%: {c8_5.get_odliczenie()}')

    print('--- Podstawa opodatkowania ---')

    c3.set_podstawa_opodatkowania()
    c5_5.set_podstawa_opodatkowania()
    c8_5.set_podstawa_opodatkowania()

    print(f'Podstawa opodatkowania 3%: {c3.get_podstawa_opodatkowania()}')
    print(f'Podstawa opodatkowania 5.5%: {c5_5.get_podstawa_opodatkowania()}')
    print(f'Podstawa opodatkowania 8.5%: {c8_5.get_podstawa_opodatkowania()}')

    print('----------------------')
    print('Podatek')

    c3.set_podatek()
    c5_5.set_podatek()
    c8_5.set_podatek()

    print(f'Podatek 3%: {c3.get_podatek()}')
    print(f'Podatek 5.5%: {c5_5.get_podatek()}')
    print(f'Podatek 8.5%: {c8_5.get_podatek()}')

    print('----------------------')
    print('Suma')

    sum = c3.get_podatek() + c5_5.get_podatek() + c8_5.get_podatek()

    print(f'Suma: {sum}')


if __name__ == "__main__":
    main()
