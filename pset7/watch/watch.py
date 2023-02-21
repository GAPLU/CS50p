import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    link = re.search(r"<iframe.+https?://(?:www\.)?youtube\.com/embed/(.+)", s)
    if link:
        first = link.group(1)
        result, scum = first.split('"', 1)
        pattern = "https://youtu.be/"
        return pattern + result
if __name__ == "__main__":
    main()