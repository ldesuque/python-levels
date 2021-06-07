from jsonschema import validate


class Car():
    def __init__(self, json_data):
        self._validate(json_data)
        self._id = json_data['id']
        self._price_per_day = json_data['price_per_day']
        self._price_per_km = json_data['price_per_km']

    def get_id(self):
        return self._id

    def get_price_per_day(self):
        return self._price_per_day

    def get_price_per_km(self):
        return self._price_per_km

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
                "price_per_day": {
                    "type": "integer"
                },
                "price_per_km": {
                    "type": "integer"
                },
            },
            "required": ["id", "price_per_day", "price_per_km"],
            "additionalProperties": False
        }

        return schema
