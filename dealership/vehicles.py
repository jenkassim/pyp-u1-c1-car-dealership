class Vehicle(object):
    def __init__(self, maker, model, year, base_price, miles):
        self.maker = maker
        self.model = model
        self.year = year
        self.base_price = base_price
        self.miles = miles

    def sale_price(self):
        return self.base_price * self.sale_multiplier

    def purchase_price(self):
        return self.sale_price() - (self.purc_multiplier * self.miles)

class Car(Vehicle):
    sale_multiplier = 1.2
    purc_multiplier = 0.004
    intr_rate = 1.07
    lease_mul = 1.2

class Motorcycle(Vehicle):
    sale_multiplier = 1.1
    purc_multiplier = 0.009
    intr_rate = 1.03
    lease_mul = 1

class Truck(Vehicle):
    sale_multiplier = 1.6
    purc_multiplier = 0.02
    intr_rate = 1.11
    lease_mul = 1.7
