def main():
    greet = input("Greeting: ")
    money = value(greet)
    print(f"${money}")

def value(greeting):
    if greeting.lower().strip().startswith("hello"):
        return int(0)
    elif greeting.lower().strip().startswith("h"):
        return int(20)
    else:
        return int(100)


if __name__ == "__main__":
    main()