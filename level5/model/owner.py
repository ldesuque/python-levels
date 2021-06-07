class Owner():
    ACTOR_WHO = 'owner'
    ACTOR_TYPE = 'credit'

    def __init__(self, rental_price, commission_fees, options_money=0):
        self._amount = int(rental_price - commission_fees) + options_money

    def get_rental_actions(self):
        return {
            "who": self.ACTOR_WHO,
            "type": self.ACTOR_TYPE,
            "amount": self._amount
        }
