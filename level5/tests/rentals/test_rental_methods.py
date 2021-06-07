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

    def test_get_rental_price_no_discount(self):
        # Given
        car_data = {"id": 1, "price_per_day": 2000, "price_per_km": 10}
        rental_data = {
            "id": 1,
            "car_id": 1,
            "start_date": "2015-12-8",
            "end_date": "2015-12-8",
            "distance": 100
        }

        # When
        car = Car(car_data)
        rental = Rental(rental_data, car)

        # Then
        self.assertEqual(3000, rental.get_rental_price())

    def test_get_rental_price_per_day_decreases_by_50(self):
        # Given
        car_data = {"id": 1, "price_per_day": 2000, "price_per_km": 10}
        rental_data = {
            "id": 3,
            "car_id": 1,
            "start_date": "2015-07-3",
            "end_date": "2015-07-14",
            "distance": 1000
        }

        # When
        car = Car(car_data)
        rental = Rental(rental_data, car)

        # Then
        self.assertEqual(27800, rental.get_rental_price())

    def test_get_commission_fees(self):
        # Given
        car_data = {"id": 1, "price_per_day": 2000, "price_per_km": 10}
        rental_data = {
            "id": 1,
            "car_id": 1,
            "start_date": "2015-12-8",
            "end_date": "2015-12-8",
            "distance": 100
        }

        # When
        car = Car(car_data)
        rental = Rental(rental_data, car)

        # Then
        self.assertEqual(
            {
                'insurance_fee': 450,
                'assistance_fee': 100,
                'drivy_fee': 350
            }, rental.get_commission_fees())

    def test_get_actions_no_options(self):
        # Given
        car_data = {"id": 1, "price_per_day": 2000, "price_per_km": 10}
        rental_data = {
            "id": 1,
            "car_id": 1,
            "start_date": "2015-12-8",
            "end_date": "2015-12-8",
            "distance": 100
        }

        # When
        car = Car(car_data)
        rental = Rental(rental_data, car)

        # Then
        self.assertEqual([{
            "who": "driver",
            "type": "debit",
            "amount": 3000
        }, {
            "who": "owner",
            "type": "credit",
            "amount": 2100
        }, {
            "who": "insurance",
            "type": "credit",
            "amount": 450
        }, {
            "who": "assistance",
            "type": "credit",
            "amount": 100
        }, {
            "who": "drivy",
            "type": "credit",
            "amount": 350
        }], rental.get_actions())

    def test_get_actions_options(self):
        # Given
        car_data = {"id": 1, "price_per_day": 2000, "price_per_km": 10}
        rental_data = {
            "id": 1,
            "car_id": 1,
            "start_date": "2015-12-8",
            "end_date": "2015-12-8",
            "distance": 100
        }

        # When
        car = Car(car_data)
        rental = Rental(rental_data, car)
        rental.set_option('gps')
        rental.set_option('baby_seat')

        # Then
        self.assertEqual([{
            "who": "driver",
            "type": "debit",
            "amount": 3700
        }, {
            "who": "owner",
            "type": "credit",
            "amount": 2800
        }, {
            "who": "insurance",
            "type": "credit",
            "amount": 450
        }, {
            "who": "assistance",
            "type": "credit",
            "amount": 100
        }, {
            "who": "drivy",
            "type": "credit",
            "amount": 350
        }], rental.get_actions())

        self.assertEqual(["gps", "baby_seat"], rental.get_options())
