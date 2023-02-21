def main():
    time = convert(input("What time is it? "))
    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")

def convert(time):
    if len(time) > 5:
        houres,minutes = time.split(":")
        minutes, time_mark = minutes.split(" ")
        if time_mark == "a.m.":
            return float(houres) + float(minutes) / 60
        elif time_mark == "p.m.":
            return 12 + float(houres) + float(minutes) / 60
    else:
        houres, minutes = time.split(":")
        return float(houres) + float(minutes) / 60

if __name__ == "__main__":
    main()