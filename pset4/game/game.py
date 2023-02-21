from random import randint

def main():
    while True:
        try:
            level = int(input("Level: "))
            if level > 0:
                break
        except ValueError:
            pass

    answer = randint(0, level)
    while True:
        try:
            guess = int(input("Guess: "))
            if guess > answer:
                print("Too large!")
            elif guess < answer:
                print("Too small!")
            else:
                print("Just right!")
                break
        except ValueError:
            pass

if __name__ == "__main__":
    main()