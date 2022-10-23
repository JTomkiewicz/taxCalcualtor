from calculator import Kalkulator


def main():
    kalkulator = Kalkulator()

    kalkulator.dodaj_kalkulator_procent(
        [2000, 200, 185, 1100, 2000, 210, - 120, 20], 0.03)
    kalkulator.dodaj_kalkulator_procent([500, 1000, 500], 0.055)
    kalkulator.dodaj_kalkulator_procent([100, 250, 200, -50], 0.085)

    kalkulator.ubezpiecznie_spoleczne = 500
    kalkulator.ubezpiecznie_zdrowotne = 150

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
