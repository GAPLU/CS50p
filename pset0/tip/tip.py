def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # convert str into float
    d = d.lstrip("$")
    return float(d)

def percent_to_float(p):
    # convert percents to rate
    p = p.rstrip("%")
    return float(p) / 100

main()