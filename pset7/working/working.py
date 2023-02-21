import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    pattern = r"^(1[0-2]|[1-9]) (AM|PM) to (1[0-2]|[1-9]) (AM|PM)$"
    match = re.match(pattern, s)
    if match:
        start_hour, start_zone, end_hour, end_zone = match.groups()
        start_hour, end_hour = int(start_hour), int(end_hour)
        start_hour = start_hour - 12 if start_zone == "AM" and start_hour == 12 else start_hour
        start_hour = start_hour + 12 if start_zone == "PM" and start_hour != 12 else start_hour
        end_hour = end_hour - 12 if end_zone == "AM" and end_hour == 12 else end_hour
        end_hour = end_hour + 12 if end_zone == "PM" and end_hour != 12 else end_hour

        return f"{start_hour:02}:00 to {end_hour:02}:00"

    else:
        pattern = r"^(1[0-2]|[1-9]):([0-5][0-9]) (AM|PM) to (1[0-2]|[1-9]):([0-5][0-9]) (AM|PM)$"
        match = re.match(pattern, s)
        if match:
            start_hour, start_minute, start_zone, end_hour, end_minute, end_zone = match.groups()
            start_hour, end_hour = int(start_hour), int(end_hour)

            if start_hour == 12 and start_minute != "00":
                raise ValueError()

            if end_hour == 12 and end_minute != "00":
                raise ValueError()

            start_hour = start_hour - 12 if start_zone == "AM" and start_hour == 12 else start_hour
            start_hour = start_hour + 12 if start_zone == "PM" and start_hour != 12 else start_hour
            end_hour = end_hour - 12 if end_zone == "AM" and end_hour == 12 else end_hour
            end_hour = end_hour + 12 if end_zone == "PM" and end_hour != 12 else end_hour

            return f"{start_hour:02}:{start_minute} to {end_hour:02}:{end_minute}"

        else:
            raise ValueError()

if __name__ == "__main__":
    main()
