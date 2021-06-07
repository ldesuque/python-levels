COMMISSION_RATE = 0.3
INSURANCE_COMMISSION_RATE = 0.5
EURO_CENTS_PER_DAY = 100


class Commission():
    def __init__(self, rental_price, rental_days):
        self._commission = rental_price * COMMISSION_RATE
        self._rental_days = rental_days

    def _get_total(self):
        return self._commission

    def _get_rental_days(self):
        return self._rental_days


class InsuranceCommission(Commission):
    def __init__(self, wrapped):
        self._wrapped = wrapped

    def get_total(self):
        return int(self._wrapped._get_total() * INSURANCE_COMMISSION_RATE)


class RoadsideAssistanceCommission(Commission):
    def __init__(self, wrapped):
        self._wrapped = wrapped

    def get_total(self):
        return self._wrapped._get_rental_days() * EURO_CENTS_PER_DAY


class CompanyCommission(Commission):
    def __init__(self, wrapped):
        self._wrapped = wrapped

    def get_total(self):
        insuranceCommission = InsuranceCommission(self._wrapped).get_total()
        roadsideCommission = RoadsideAssistanceCommission(
            self._wrapped).get_total()

        return int(self._wrapped._get_total() - insuranceCommission -
                   roadsideCommission)
