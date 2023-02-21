vowels = ['a', 'i', 'u', 'e', 'o', 'A', 'I', 'U', 'E', 'O']

def main():
    word = input("Input: ")
    print("Output: ", end="")
    word = shorten(word)
    print(word)

def shorten(word):
    for vowel in vowels:
        word = word.replace(vowel, '')
    return word

if __name__ == "__main__":
    main()