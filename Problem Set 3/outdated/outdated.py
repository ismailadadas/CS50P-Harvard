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
        month, day, year = date.split("/")

    elif "," in date:
        month, day, year = date.split()

        if month in months: 
            month = months.index(month)
            month += 1 
            day = day.strip(",")

        else:
            continue
        try:

            if int(day) > 31 or int(month) > 12: 
                continue

            else: 
                break

        except ValueError:
            continue
month = int(month)
day = int(day)

print(f"{year}-{month:02}-{day:02}")