import unittest

from model.car import Car


class TestCarMethods(unittest.TestCase):
    def test_get_id(self):
        # Given
        car_data = {"id": 1, "price_per_day": 2000, "price_per_km": 10}

        # When
        car = Car(car_data)

        # Then
        self.assertEqual(1, car.get_id())

    def test_get_price_per_day(self):
        # Given
        car_data = {"id": 1, "price_per_day": 2000, "price_per_km": 10}

        # When
        car = Car(car_data)

        # Then
        self.assertEqual(2000, car.get_price_per_day())

    def test_get_price_per_km(self):
        # Given
        car_data = {"id": 1, "price_per_day": 2000, "price_per_km": 10}

        # When
        car = Car(car_data)

        # Then
        self.assertEqual(10, car.get_price_per_km())