from tax_calculator import TaxCalculator


def get_input_data() -> TaxCalculator:
    rates: list = [0.03, 0.055, 0.085, 0.12, 0.14, 0.15, 0.17]

    kalkulator = TaxCalculator()

    print('Enter 0 to go to the following lump sum (podaj 0 aby przejsc do nastepnej stawki ryczaltu)')

    for rate in rates:
        costs: list = []
        while True:
            try:
                cost = int(
                    input(f'Input cost for rate (kwota dla stawki) {round(rate * 100, 1)}%: '))
            except ValueError:
                print("Error occured (wystapil blad)")

            if cost == 0:
                break
            costs.append(cost)

        if costs:
            kalkulator.set_costs_for_rate(costs, rate)

    paid_social_security = input(
        'Input paid social security (oplacone ubezpieczenie spolecze): ')
    kalkulator.set_paid_social_security(paid_social_security)

    paid_health_insurance = input(
        'Input paid health insurance (oplacone ubezpieczenie zdrowotne): ')
    kalkulator.set_paid_health_insurance(paid_health_insurance)

    return kalkulator


def main():
    kalkulator = get_input_data()

    print('--- revenues according to tax rates (przychody wg stawek) ---')
    kalkulator.calculate_revenue_tax_rates()

    print('--- revenue structure (struktura przychodow) ---')
    kalkulator.calculate_revenue_structure()

    print('--- deductions (odliczenia) ---')
    kalkulator.calculate_ss_hi_deduction()
    kalkulator.calculate_deductions()

    print('--- tax base (podstawa opodatkowania) ---')
    kalkulator.calculate_tax_base()

    print('--- tax grouped into rates (podatek pogrupowany na stawki) ---')
    kalkulator.calculate_tax_rates()

    print('--- tax sum (suma podatku) ---')
    kalkulator.calculate_tax_sum()


if __name__ == "__main__":
    main()
