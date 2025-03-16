
class Bill:

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, days_flatmate2):
        days = self.days_in_house / (self.days_in_house + days_flatmate2)
        total = days * bill.amount
        return total
