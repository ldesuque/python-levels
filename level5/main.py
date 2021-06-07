from app import App
from utils.file_utils import read_file, write_file

INPUT_FILE = "./data/input.json"
OUTPUT_FILE = "./data/output.json"


def main():
    data_input = read_file(INPUT_FILE)

    app = App(data_input)
    report = app.get_rentals_report()

    write_file(report, OUTPUT_FILE)


if __name__ == "__main__":
    main()
