import csv
import argparse

# def openAndRead(file):
#     with open(file, mode='r', newline='') as f:
#         reader = csv.DictReader(f)

def convertFirstLetterToSmall(dict_list):
    for dict in dict_list:
        for key in dict:
            dict[key] = dict[key].lower()
    return dict_list

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
            print(row['Name'])

def main():

    parser = argparse.ArgumentParser(description="process a csv file and ask questions.")
    parser.add_argument('file', type=str, help='path to the csv file')
    args = parser.parse_args()

    data = convertFirstLetterToSmall(readCsv(args.file))
    print(data)

    while True:
        column_name = input("enter the column name (or'exit' to quit):")

        if column_name.lower() == 'exit':
            break

        value = input(f"enter the value to search for in column '{column_name}': ").lower()
        printValue(data, column_name, value)



if __name__ == "__main__":
    main()
