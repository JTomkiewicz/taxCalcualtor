from tax_calculator import TaxCalculator


def get_input_data() -> TaxCalculator:
    rates: list = [0.03, 0.055, 0.085, 0.12, 0.14, 0.15, 0.17]

    tc = TaxCalculator()

    print('Enter 0 to go to the following lump sum (podaj 0 aby przejsc do nastepnej stawki ryczaltu)')

    for rate in rates:
        costs: list = []
        while True:
            try:
                cost = int(
                    input(f'Input cost for rate (kwota dla stawki) {round(rate * 100, 1)}%: '))
            except ValueError:
                print("ValueError! Try again!")

            if cost == 0:
                break
            costs.append(cost)

        if costs:
            tc.set_costs_for_rate(costs, rate)

    while True:
        try:
            paid_social_security = float(input(
                'Input paid social security (oplacone ubezpieczenie spolecze): '))
            break
        except ValueError:
            print("ValueError! Try again!")

    tc.set_paid_social_security(paid_social_security)

    while True:
        try:
            paid_health_insurance = float(input(
                'Input paid health insurance (oplacone ubezpieczenie zdrowotne): '))
            break
        except ValueError:
            print("ValueError! Try again!")

    tc.set_paid_health_insurance(paid_health_insurance)

    return tc


def main():
    tc = get_input_data()

    print('\n--- revenues according to tax rates (przychody wg stawek) ---\n')
    tc.calculate_revenue_tax_rates()

    print('\n--- revenue structure (struktura przychodow) ---\n')
    tc.calculate_revenue_structure()

    print('\n--- deductions (odliczenia) ---\n')
    tc.calculate_ss_hi_deduction()
    tc.calculate_deductions()

    print('\n--- tax base (podstawa opodatkowania) ---\n')
    tc.calculate_tax_base()

    print('\n--- tax grouped into rates (podatek pogrupowany na stawki) ---\n')
    tc.calculate_tax_rates()

    print('\n--- tax sum (suma podatku) ---\n')
    tc.calculate_tax_sum()
    print()


if __name__ == "__main__":
    main()
