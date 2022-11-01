class RateCalculator():
    def __init__(self, costs: list, rate: float) -> None:
        self.costs: float = costs
        self.rate: float = rate
        self.costs_sum: float = self.set_costs_sum()
        self.revenue_structure: float = 0.0
        self.deduction: float = 0.0
        self.tax_base: float = 0.0
        self.tax_rate: float = 0.0

    def set_costs_sum(self) -> float:
        sum = 0
        for cost in self.costs:
            sum += cost
        return sum

    def set_revenue_structure(self, revenue_tax_rates_sum: float) -> None:
        self.revenue_structure = round(
            self.costs_sum / revenue_tax_rates_sum, 2)

    def set_deduction(self, deductions_sum: float) -> None:
        self.deduction = round(self.revenue_structure * deductions_sum, 2)

    def set_tax_base(self) -> None:
        self.tax_base = int(
            self.costs_sum - self.deduction)

    def set_tax_rate(self) -> None:
        self.tax_rate = round(self.rate * self.tax_base, 2)
