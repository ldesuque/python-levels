import json

from model.car import Car
from model.rental import Rental

INPUT_FILE = "./data/input.json"
OUTPUT_FILE = "./data/output.json"


def read_file():
    with open(INPUT_FILE) as json_input:
        data_input = json.load(json_input)

    return data_input


def write_file(data):
    with open(OUTPUT_FILE, 'w') as output_file:
        json.dump(data, output_file)


def get_cars_from_data(data_input):
    cars = []

    for data_car in data_input['cars']:
        cars.append(Car(data_car))

    return cars


def get_rentals_from_data(data_input, cars):
    rentals = []

    for data_rental in data_input['rentals']:
        car = next(car for car in cars
                   if car.get_id() == data_rental['car_id'])
        rentals.append(Rental(data_rental, car))

    return rentals


def get_rental_prices(rentals):
    rentals_prices = {}
    rentals_prices['rentals'] = []

    for rental in rentals:
        rentals_prices['rentals'].append({
            'id':
            rental.get_id(),
            'price':
            rental.get_rental_price(),
            'commission':
            rental.get_commission_fees()
        })

    return rentals_prices


def main():
    data_input = read_file()

    cars = get_cars_from_data(data_input)
    rentals = get_rentals_from_data(data_input, cars)
    rental_prices = get_rental_prices(rentals)

    write_file(rental_prices)


if __name__ == "__main__":
    main()
