from model.actor import Actor


class Driver(Actor):
    ACTOR_WHO = 'driver'
    ACTOR_TYPE = 'debit'

    def __init__(self, amount):
        self._amount = amount

    def get_rental_actions(self):
        return {
            "who": self.ACTOR_WHO,
            "type": self.ACTOR_TYPE,
            "amount": self._amount
        }
