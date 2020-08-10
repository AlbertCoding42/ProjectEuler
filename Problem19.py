# Produce list of days from 1st of Jan 1901 onwards:

days = []

for i in range(0, 6000):
    days.append("tue")
    days.append("wed")
    days.append("thu")
    days.append("fri")
    days.append("sat")
    days.append("sun")
    days.append("mon")
sun_total = 0
year = 1900
month = "jan"
a = 0
while year != 2001:
    # Checks every first day of the month to see if that day is a sunday:
    if month == "jan":
        if days[a] == "sun":
            sun_total += 1
        a += 31
        month = "Feb"
        year += 1
        # print(year)
    elif month == "Feb":
        month = "Mar"
        if year%4 == 0:
            if days[a] == "sun":
                sun_total += 1
            a += 29
        elif year%4 != 0:
            if days[a] == "sun":
                sun_total += 1
            a += 28
    elif month == "Mar":
        if days[a] == "sun":
            sun_total += 1
        a += 31
        month = "Apr"
    elif month == "Apr":
        if days[a] == "sun":
            sun_total += 1
        a += 30
        month = "May"
    elif month == "May":
        if days[a] == "sun":
            sun_total += 1
        a += 31
        month = "Jun"
    elif month == "Jun":
        if days[a] == "sun":
            sun_total += 1
        a += 30
        month = "Jul"
    elif month == "Jul":
        if days[a] == "sun":
            sun_total += 1
        a += 31
        month = "Aug"
    elif month == "Aug":
        if days[a] == "sun":
            sun_total += 1
        a += 31
        month = "Sep"
    elif month == "Sep":
        if days[a] == "sun":
            sun_total += 1
        a += 30
        month = "Oct"
    elif month == "Oct":
        if days[a] == "sun":
            sun_total += 1
        a += 31
        month = "Nov"
    elif month == "Nov":
        if days[a] == "sun":
            sun_total += 1
        a += 30
        month = "Dec"
    elif month == "Dec":
        if days[a] == "sun":
            sun_total += 1
        a += 31
        month = "jan"

#Prints the number of times a sunday landed on the first day of the month in the 20th Century:

print(sun_total)




