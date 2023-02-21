def main():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    while True:
        date = input("Date: ")
        try:
            month, day, year = date.split("/")
            month = int(month)
            day = int(day)
            if 1 <= month <= 12 and 1 <= day <= 31:
                break
        except ValueError:
            try:
                month, day, year = date.split(" ")
                day,_ = day.split(",")
                day = int(day)
                if 1 <= day <= 31 and month in months:
                    month = months.index(month) + 1
                    break
            except ValueError:
                pass
            pass

    print(year.strip(), f"{month:02}", f"{day:02}", sep="-")

main()