import inflect

p = inflect.engine()


def main():
    names = []
    while True:
        try:
            alias = input("Name: ")
            names.append(alias)
        except EOFError:
            names_list = p.join(names)
            print("Adieu, adieu, to", names_list)
            break


if __name__ == "__main__":
    main()