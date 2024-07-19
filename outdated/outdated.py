#year-month-day september 8, 1674
months=[
    "January" ,
    "February",
    "March",
    "April"
    ,"May",
    "June" ,
    "July" ,
    "August" ,
    "September" ,
    "October" ,
    "November" ,
    "December"
]
while True:
    date=input("Date:")
    if "/" in date:
        month , day , year = date.split("/")

    elif "," in date:
        date=date.replace(",", "")
        month, day, year = date.split(" ")
        if month in months:
            month=months.index(month)+1
    else:
        continue

    try:
        if int(day) > 31 or int(month) > 12:
            continue
        else:
            break
    except ValueError:
        continue
print(f"{int(year)}" + "-" + f"{int(month):02}" + "-" + f"{int(day):02}")


