from model.actor import Actor


class Owner(Actor):
    ACTOR_WHO = 'owner'
    ACTOR_TYPE = 'credit'

    def __init__(self, amount):
        self._amount = int(amount)

    def get_rental_actions(self):
        return {
            "who": self.ACTOR_WHO,
            "type": self.ACTOR_TYPE,
            "amount": self._amount
        }
