from jsonschema import validate

from model.car import Car
from model.commission import Commission, InsuranceCommission, RoadsideAssistanceCommission, CompanyCommission
from utils.period_in_days import period_in_days

DISCOUNT_RATE_10 = 0.9
DISCOUNT_RATE_30 = 0.7
DISCOUNT_RATE_50 = 0.5


class Rental():
    def __init__(self, json_data, car):
        self._validate(json_data)
        self._id = json_data['id']
        self._start_date = json_data['start_date']
        self._end_date = json_data['end_date']
        self._distance = json_data['distance']
        self._car = car

    def get_id(self):
        return self._id

    def get_commission_fees(self):
        rental_price = self.get_rental_price()
        rental_days = self._get_rental_days()
        commission = Commission(rental_price, rental_days)

        insuranceCommission = InsuranceCommission(commission)
        insurance_fee = insuranceCommission.get_total()

        assistanceCommission = RoadsideAssistanceCommission(commission)
        assistance_fee = assistanceCommission.get_total()

        companyCommission = CompanyCommission(commission)
        drivy_fee = companyCommission.get_total()

        return {
            'insurance_fee': insurance_fee,
            'assistance_fee': assistance_fee,
            'drivy_fee': drivy_fee
        }

    def get_rental_price(self):
        distance_component = self._car.get_price_per_km() * self._distance
        total = self._get_total_price_per_day() + distance_component

        return total

    def _get_total_price_per_day(self):
        total = 0
        rental_days = self._get_rental_days()

        for i in range(1, rental_days + 1):
            total += self._get_new_price_with_discount(i)

        return int(total)

    def _get_new_price_with_discount(self, rental_day):
        price_per_day = self._car.get_price_per_day()
        selector = {
            lambda rd: 1 == rd: price_per_day,
            lambda rd: 1 < rd <= 4: price_per_day * DISCOUNT_RATE_10,
            lambda rd: 4 < rd <= 10: price_per_day * DISCOUNT_RATE_30,
            lambda rd: rd > 10: price_per_day * DISCOUNT_RATE_50
        }

        selected = [selector[d] for d in selector if d(rental_day)]
        return selected[0]

    def _get_rental_days(self):
        return period_in_days(self._start_date, self._end_date)

    def _validate(self, json_data):
        validate(instance=json_data, schema=self._json_schema())

    def _json_schema(self):
        schema = {
            "type": "object",
            "properties": {
                "id": {
                    "type": "integer",
                    "minimum": 0
                },
                "car_id": {
                    "type": "integer",
                    "minimum": 0
                },
                "start_date": {
                    "type": "string"
                },
                "end_date": {
                    "type": "string"
                },
                "distance": {
                    "type": "integer"
                },
            },
            "required": ["id", "car_id", "start_date", "end_date", "distance"],
            "additionalProperties": False
        }

        return schema
