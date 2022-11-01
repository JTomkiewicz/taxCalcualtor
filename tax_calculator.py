from rate_calculator import RateCalculator


class TaxCalculator():
    def __init__(self):
        self.rate_calculators: list = []
        self.paid_social_security: float = 0.0
        self.paid_health_insurance: float = 0.0
        self.revenue_tax_rates_sum: float = 0.0
        self.deduction: float = 0.0

    def set_costs_for_rate(self, costs: list, rate: float) -> None:
        self.rate_calculators.append(RateCalculator(costs, rate))

    def set_paid_social_security(self, paid_social_security: float):
        self.paid_social_security = paid_social_security

    def set_paid_health_insurance(self, paid_health_insurance: float):
        self.paid_health_insurance = paid_health_insurance

    def calculate_revenue_tax_rates(self):
        for obj in self.rate_calculators:
            print(f'{obj.rate * 100}%: {obj.costs_sum} PLN')
            self.revenue_tax_rates_sum += obj.costs_sum
        print(
            f'Revenue tax rates sum (suma przychodu): {self.revenue_tax_rates_sum} PLN')

    def calculate_revenue_structure(self):
        for obj in self.rate_calculators:
            obj.set_revenue_structure(self.revenue_tax_rates_sum)
            print(
                f'{obj.rate * 100}%: {obj.costs_sum} / {self.revenue_tax_rates_sum} = {int(obj.revenue_structure * 100)} %')

    def calculate_ss_hi_deduction(self):
        self.deduction = round(self.paid_social_security +
                               (0.5 * self.paid_health_insurance), 2)

    def calculate_deductions(self):
        for obj in self.rate_calculators:
            obj.set_deduction(self.deduction)
            print(
                f'{obj.rate * 100}%: {obj.revenue_structure * 100} % * {self.deduction} = {obj.deduction} PLN')

    def calculate_tax_base(self):
        for obj in self.rate_calculators:
            obj.set_tax_base()
            print(
                f'{obj.rate * 100}%: {obj.costs_sum} - {obj.deduction} = {obj.tax_base} PLN')

    def calculate_tax_rates(self):
        for obj in self.rate_calculators:
            obj.set_tax_rate()
            print(
                f'{obj.rate * 100}% * {obj.tax_base} = {obj.tax_rate} PLN')

    def calculate_tax_sum(self):
        sum: float = 0.0
        for obj in self.rate_calculators:
            sum += obj.tax_rate
        print(f'Tax sum (suma podatku): {round(sum, 2)} PLN')
