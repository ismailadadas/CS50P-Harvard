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
    date = input("Date: ").strip()

    if "/" in date:
        try:
            month, day, year = date.split("/")
            month = int(month)
            day = int(day)
            year = int(year)
        except ValueError:
            continue  

    elif "," in date:
        try:
            month_name, day, year = date.split()
            if month_name in months:
                month = months.index(month_name) + 1
                day = int(day.strip(","))
                year = int(year)
            else:
                continue
        except ValueError:
            continue

    else:
        continue


    if not (1 <= month <= 12 and 1 <= day <= 31):
        continue

    break

print(f"{year}-{month:02}-{day:02}")
