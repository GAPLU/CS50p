from tabulate import tabulate
import sys
import csv

def main():
    pizzas = []

    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif sys.argv[1][-4:] != ".csv":
        sys.exit("Not a CSV file")


    try:
        file = open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("File does not exist")

    reader = csv.reader(file)
    for type, small, large in reader:
        pizzas.append([type, small, large])


    print(tabulate(pizzas, headers="firstrow", tablefmt="grid"))



if __name__ == "__main__":
    main()