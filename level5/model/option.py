class Option():
    NO_PROFIT = 0
    EURO_CENTS = 100

    def __init__(self, rental_days):
        self._rental_days = rental_days

    def _get_rental_days(self):
        return self._rental_days


class GPS(Option):
    PRICE_PER_DAY_EURO = 5
    OPTION_TYPE = 'gps'

    def __init__(self, rental_days):
        super().__init__(rental_days)

    def get_money_to_owner(self):
        return self._get_rental_days(
        ) * self.PRICE_PER_DAY_EURO * self.EURO_CENTS

    def get_money_to_company(self):
        return self.NO_PROFIT

    def get_type(self):
        return self.OPTION_TYPE


class BabySeat(Option):
    PRICE_PER_DAY_EURO = 2
    OPTION_TYPE = 'baby_seat'

    def __init__(self, rental_days):
        super().__init__(rental_days)

    def get_money_to_owner(self):
        return self._get_rental_days() * self.PRICE_PER_DAY_EURO * self.EURO_CENTS

    def get_money_to_company(self):
        return self.NO_PROFIT

    def get_type(self):
        return self.OPTION_TYPE


class AdditionalInsurance(Option):
    PRICE_PER_DAY_EURO = 10
    OPTION_TYPE = 'additional_insurance'

    def __init__(self, rental_days):
        super().__init__(rental_days)

    def get_money_to_owner(self):
        return self.NO_PROFIT

    def get_money_to_company(self):
        return self._get_rental_days() * self.PRICE_PER_DAY_EURO * self.EURO_CENTS

    def get_type(self):
        return self.OPTION_TYPE
