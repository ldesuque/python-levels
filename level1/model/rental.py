from jsonschema import validate

from model.car import Car
from utils.period_in_days import period_in_days


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

    def get_rental_price(self):
        time_component = self._car.get_price_per_day() * self._get_rental_days(
        )
        distance_component = self._car.get_price_per_km() * self._distance

        return time_component + distance_component

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
