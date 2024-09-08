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