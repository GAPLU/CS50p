import datetime
import sys
import inflect

p = inflect.engine()

def main():
    birth = input("Date of Birth: ")
    print(lifetime(birth) + " minutes")


def lifetime(s):
    try:
        birth = datetime.date.fromisoformat(s)
    except ValueError:
        return sys.exit("Invalid date")

    today = datetime.date.today()
    time_alive = today - birth
    seconds_alive = time_alive.total_seconds()
    minutes_alive = int(round(seconds_alive / 60))
    return p.number_to_words(minutes_alive, andword="").capitalize()

if __name__ == "__main__":
    main()