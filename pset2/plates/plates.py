def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    for _ in range(len(s) - 1):
        if not s[_].isalpha() and not s[_].isdigit():
            return False
        if s[_].isdigit():
            if s[_ + 1].isalpha():
                return False
            if s[_ - 1].isalpha() and s[_] == "0":
                return False

    if not s[0:2].isalpha():
        return False
    elif not 2 <= len(s) <= 6:
        return False
    else:
        return True

main()