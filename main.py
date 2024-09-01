import csv
import argparse

def readCsv(file_path):
    data = []
    with open(file_path, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

def printValue(data, column_name, value):
    for row in data:
        if row.get(column_name) == value:
            print(row)


def main():

    parser = argparse.ArgumentParser(description="process a csv file and ask questions.")
    parser.add_argument('file', type=str, help='path to the csv file')
    args = parser.parse_args()

    data = readCsv(args.file)

    while True:
        column_name = input("enter the column name (or'exit' to quit):").strip()

        if column_name.lower() == 'exit':
            break

        value = input(f"enter the value to search for in column '{column_name}': ").strip()
        printValue(data, column_name, value)


if __name__ == "__main__":
    main()
