def main():
    greet = input("Greeting: ")
    if greet.lower().strip().startswith("hello"):
        print("$0")
    elif greet.lower().strip().startswith("h"):
        print("$20")
    else:
        print("$100")

main()