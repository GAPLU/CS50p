import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    ip_proof = re.search(r"^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])$", ip)

    if ip_proof:
        return True
    else:
        return False


if __name__ == "__main__":
    main()