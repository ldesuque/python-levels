class Driver():
    ACTOR_WHO = 'driver'
    ACTOR_TYPE = 'debit'

    def __init__(self, amount, options_money=0):
        self._amount = amount + options_money

    def get_rental_actions(self):
        return {
            "who": self.ACTOR_WHO,
            "type": self.ACTOR_TYPE,
            "amount": self._amount
        }
