from model.car import Car
from model.rental import Rental
from model.option import GPS, BabySeat, AdditionalInsurance


class App():
    def __init__(self, data_input):
        self._cars = self._get_cars_from_data(data_input)
        self._rentals = self._get_rentals_from_data(data_input)
        self._set_options_from_data(data_input)

    def get_rentals_report(self):
        report = {}
        report['rentals'] = []

        for rental in self._rentals:
            report['rentals'].append({
                'id': rental.get_id(),
                'options': rental.get_options(),
                'actions': rental.get_actions(),
            })

        return report

    def _get_cars_from_data(self, data_input):
        cars = []

        for data_car in data_input['cars']:
            cars.append(Car(data_car))

        return cars

    def _get_rentals_from_data(self, data_input):
        rentals = []

        for data_rental in data_input['rentals']:
            car = next(car for car in self._cars
                       if car.get_id() == data_rental['car_id'])
            rentals.append(Rental(data_rental, car))

        return rentals

    def _set_options_from_data(self, data_input):
        options = []

        for data_options in data_input['options']:
            rental = next(rental for rental in self._rentals
                          if rental.get_id() == data_options['rental_id'])

            option_type = data_options['type']
            rental.set_option(option_type)
