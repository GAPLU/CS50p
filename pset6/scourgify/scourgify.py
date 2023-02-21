import csv
import sys

def main():
    students = []
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    try:
        file = open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Could not read invalid_file.csv")

    reader = csv.DictReader(file)

    for row in reader:
        last, first = row["name"].split(", ")
        students.append({"first": first, "last": last, "house": row["house"]})

    with open(sys.argv[2], "w") as file_out:
        writer = csv.DictWriter(file_out, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for student in students:
            writer.writerow(student)



if __name__ == "__main__":
    main()