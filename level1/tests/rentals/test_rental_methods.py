import unittest

from model.car import Car
from model.rental import Rental


class TestRentalMethods(unittest.TestCase):
    def test_get_id(self):
        # Given
        car_data = {"id": 1, "price_per_day": 2000, "price_per_km": 10}
        rental_data = {
            "id": 1,
            "car_id": 1,
            "start_date": "2017-12-8",
            "end_date": "2017-12-10",
            "distance": 100
        }

        # When
        car = Car(car_data)
        rental = Rental(rental_data, car)

        # Then
        self.assertEqual(1, rental.get_id())

    def test_get_rental_price(self):
        # Given
        car_data = {"id": 1, "price_per_day": 2000, "price_per_km": 10}
        rental_data = {
            "id": 1,
            "car_id": 1,
            "start_date": "2017-12-8",
            "end_date": "2017-12-10",
            "distance": 100
        }

        # When
        car = Car(car_data)
        rental = Rental(rental_data, car)

        # Then
        self.assertEqual(7000, rental.get_rental_price())