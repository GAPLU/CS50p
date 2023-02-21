import emoji

def main():
    text = input("Input: ")
    if "_" in text:
        print("Output:", emoji.emojize(text))
    else:
        print("Output:", emoji.emojize(text, language="alias"))

if __name__ == "__main__":
    main()