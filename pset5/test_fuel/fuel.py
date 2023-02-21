def main():
    while True:
        rate = input("Fraction:" )
        result = convert(rate)
        if result or result == 0:
            break

    print(gauge(result))


def convert(fraction):
    try:
        p1, p2 = fraction.split("/")
        result = int(round((int(p1) / int(p2)) * 100))
        if 0 <= result <= 100:
            return result
        else:
            raise ValueError("False")

    except ValueError:
        raise ValueError("False")
    except ZeroDivisionError:
        raise ZeroDivisionError("False")


def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()