import sys

def main():
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif sys.argv[1][-3:] != ".py":
        sys.exit("Not a Python file")
    elif not sys.argv[1]:
        sys.exit("Too few command-line arguments")

    try:
        file = open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("File does not exist")

    file_len = 0
    for row in file:
        if row.lstrip().startswith("#") == False and row.strip():
            file_len += 1
    print(file_len)


if __name__ == "__main__":
    main()