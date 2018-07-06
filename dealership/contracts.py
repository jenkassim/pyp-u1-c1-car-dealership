class Contract(object):
    def __init__(self, vehicle, customer):
        self.vehicle = vehicle
        self.customer = customer

    def total_value(self):
        disc = 0
        if self.customer.is_employee():
            disc = 0.10 * self._total_value()

        return self._total_value() - disc

    def monthly_value(self):
        return self.total_value() / self._monthly_value()


class BuyContract(Contract):
    def __init__(self, vehicle, customer, monthly_payments):
        super(BuyContract, self).__init__(vehicle,customer)
        self.monthly_payments = monthly_payments

    def _total_value(self):
        sale_price = self.vehicle.sale_price()

        return sale_price + (self.vehicle.intr_rate * self.monthly_payments * sale_price / 100)

    def _monthly_value(self):
        return self.monthly_payments


class LeaseContract(Contract):
    def __init__(self, vehicle, customer, length_in_months):
        super(LeaseContract, self).__init__(vehicle, customer)
        self.length_in_months = length_in_months

    def _total_value(self):
        sale_price = self.vehicle.sale_price()
        return sale_price + (sale_price * self.vehicle.lease_mul / self.length_in_months)

    def _monthly_value(self):
        return self.length_in_months
