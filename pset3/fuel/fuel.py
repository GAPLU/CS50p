def main():
    while True:
        rate = input("Fraction:" )
        try:
            p1, p2 = rate.split("/")
            result = int(round((int(p1) / int(p2)) * 100))
            if 0 <= result <= 100:
                break
        except (ValueError, ZeroDivisionError):
            pass

    if result >= 99:
        print("F")
    elif result <= 1:
        print("E")
    else:
        print(result, "%", sep="")

main()