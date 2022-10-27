from kalkulator import Kalkulator


def dane_wejciowe() -> Kalkulator:
    stawki: list = [0.03, 0.055, 0.085, 0.12, 0.14, 0.15, 0.17]

    kalkulator = Kalkulator()

    print('Podawanie stawek. Wpisz 0, aby zakonczyc podwanie kwot dla konkretnej stawki.')

    for stawka in stawki:
        kwoty: list = []
        while True:
            try:
                kwota = int(
                    input(f'Podaj kwote dla stawki {round(stawka * 100, 1)}%: '))
            except ValueError:
                print("Sorry, I didn't understand that.")

            if kwota == 0:
                break
            kwoty.append(kwota)

        if kwoty:
            kalkulator.dodaj_kalkulator_procent(kwoty, stawka)

    ubezpieczenie_spoleczne = input('Podaj kwote ubezpieczenia spoleczengo: ')
    kalkulator.dodaj_ubezpieczenie_spoleczne(ubezpieczenie_spoleczne)

    ubezpieczenie_zdrowotne = input('Podaj kwote ubezpieczenia zdrowotnego: ')
    kalkulator.dodaj_ubezpieczenie_spoleczne(ubezpieczenie_zdrowotne)

    return kalkulator


def main():
    kalkulator = dane_wejciowe()

    print('--- Przychody wg stawek ---')
    kalkulator.licz_przychody_wg_stawek()

    print('--- Struktura przychodow ---')
    kalkulator.licz_struktura_przychodow()

    print('--- Rozliczenie odliczen ---')
    kalkulator.licz_odliczenia()
    kalkulator.licz_rozliczenie_odliczen()

    print('--- Podstawa opodatkowania ---')
    kalkulator.licz_podstawa_opodatkowania()

    print('--- Podatek ---')
    kalkulator.licz_podatek()

    print('--- Suma ---')
    kalkulator.licz_suma_podatku()


if __name__ == "__main__":
    main()
