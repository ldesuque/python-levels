import json


def read_file(input_file):
    with open(input_file) as json_input:
        data_input = json.load(json_input)

    return data_input


def write_file(data, output_file):
    with open(output_file, 'w') as file:
        json.dump(data, file)