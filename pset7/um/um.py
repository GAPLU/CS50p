import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    pattern = r"\bum\b"
    match = re.findall(pattern, s,flags=re.IGNORECASE)
    if match:
        return(len(match))
    else:
        return 0

if __name__ == "__main__":
    main()