import random


def main():
    level = get_level()
    score = 0
    for _ in range(10):
        fails = 0
        number_1 = generate_integer(level)
        number_2 = generate_integer(level)
        sum = number_1 + number_2
        while True:
            try:
                answer = int(input(f"{number_1} + {number_2} = "))
                if answer != sum:
                    print("EEE")
                    fails += 1
                    if fails == 3:
                        print(sum)
                        break
                else:
                    score += 1
                    break
            except ValueError:
                pass

    print("Score:", score)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 1 <= level <= 3:
                return level
        except ValueError:
            pass


def generate_integer(level):
    match level:
        case 1:
            return random.randint(0, 9)
        case 2:
            return random.randint(10, 99)
        case 3:
            return random.randint(100, 999)


if __name__ == "__main__":
    main()
