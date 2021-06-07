from model.actor import Actor


class Commission(Actor):
    COMMISSION_RATE = 0.3

    def __init__(self, rental_price, rental_days):
        self._commission = rental_price * self.COMMISSION_RATE
        self._rental_days = rental_days

    def get_total(self):
        return self._commission

    def _get_rental_days(self):
        return self._rental_days

    @classmethod
    def get_rental_actions(cls):
        raise NotImplementedError('Subclass responsability')


class InsuranceCommission(Commission):
    INSURANCE_COMMISSION_RATE = 0.5
    ACTOR_WHO = 'insurance'
    ACTOR_TYPE = 'credit'

    def __init__(self, wrapped):
        self._wrapped = wrapped

    def get_total(self):
        return int(self._wrapped.get_total() * self.INSURANCE_COMMISSION_RATE)

    def get_rental_actions(self):
        return {
            "who": self.ACTOR_WHO,
            "type": self.ACTOR_TYPE,
            "amount": self.get_total()
        }


class RoadsideAssistanceCommission(Commission):
    EURO_CENTS_PER_DAY = 100
    ACTOR_WHO = 'assistance'
    ACTOR_TYPE = 'credit'

    def __init__(self, wrapped):
        self._wrapped = wrapped

    def get_total(self):
        return self._wrapped._get_rental_days() * self.EURO_CENTS_PER_DAY

    def get_rental_actions(self):
        return {
            "who": self.ACTOR_WHO,
            "type": self.ACTOR_TYPE,
            "amount": self.get_total()
        }


class CompanyCommission(Commission):
    ACTOR_WHO = 'drivy'
    ACTOR_TYPE = 'credit'

    def __init__(self, wrapped):
        self._wrapped = wrapped

    def get_total(self):
        insuranceCommission = InsuranceCommission(self._wrapped).get_total()
        roadsideCommission = RoadsideAssistanceCommission(
            self._wrapped).get_total()

        return int(self._wrapped.get_total() - insuranceCommission -
                   roadsideCommission)

    def get_rental_actions(self):
        return {
            "who": self.ACTOR_WHO,
            "type": self.ACTOR_TYPE,
            "amount": self.get_total()
        }
