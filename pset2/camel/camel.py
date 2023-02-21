def main():
    text = input("camelCase: ")

    for _ in range(len(text)):
        if text[_].isupper():
            print("_" + text[_].lower(), end="")
        else:
            print(text[_], end="")
    print()

if __name__ == "__main__":
    main()