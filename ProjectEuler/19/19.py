import fileinput

def isLeapYear(year):
    if (year % 4 == 0):
        if (year % 100 == 0):
            if (year % 400 == 0):
                return True
            else:
                return False
        else:
            return True
    return False

def daysInYear(year):
    if (isLeapYear(year)):
        return 366
    else:
        return 365

def daysInMonth(month, year):
    daysPerMonth =     [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    daysPerMonthLeap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if (isLeapYear(year)):
        return daysPerMonthLeap[month]
    else:
        return daysPerMonth[month]

def daysBetweenOld(date1, date2):
    day1, mon1, year1 = date1[0], date1[1], date1[2]
    day2, mon2, year2 = date2[0], date2[1], date2[2]

    days = 0

    # fix days
    tempyear2 = year2
    while (day1 > day2):
        day2 += daysInMonth(mon2, year2)
        mon2 -= 1

    # fix months
    tempmon2 = mon2
    if (mon1 > mon2):
        tempmon2 = mon2 + 12
        tempyear2 -= 1

    #print (day1, mon1, year1)
    #print (day2, tempmon2, tempyear2)

    # calculate years in days
    for i in xrange(year1, tempyear2):
        days += daysInYear(i)

    # calculate months in days
    for i in xrange(mon1 + 1, tempmon2):
        if (i % 12 > mon1):
            days += daysInMonth(i%12, year1)
        else:
            days += daysInMonth(i%12, year2)

    # calculate days
    days += daysInMonth(mon1, year1) - day1
    days += day2

    return days

def daysBetween(date1, date2):
    day1, mon1, year1 = date1[0], date1[1], date1[2]
    day2, mon2, year2 = date2[0], date2[1], date2[2]

    a1 = (14 - mon1)//12
    y1 = year1 + 4800 - a1
    m1 = mon1 + 12 * a1 - 3
    jdn1 = day1 + (153 * m1 + 2)//5 + 365 * y1 + y1//4 - y1//100 + y1//400 - 32045

    a2 = (14 - mon2)//12
    y2 = year2 + 4800 - a2
    m2 = mon2 + 12 * a2 - 3
    jdn2 = day2 + (153 * m2 + 2)//5 + 365 * y2 + y2//4 - y2//100 + y2//400 - 32045

    return jdn2 - jdn1

#date1 = (5, 11, 1000)
#date2 = (15, 10, 2004)
#print(daysBetweenOld(date1, date2))

def isSunday(day, month, year):
    #date1 = (0, 6, 1900) # 1 jan 1900 was a monday, 7 was a sunday
    date1 = (1, 7, 1900)
    date2 = (day, month, year)
    numDaysBetween = daysBetween(date1, date2)
    if (numDaysBetween % 7 == 0):
        return True
    return False

sunCount = 0
for yr in xrange(1901, 2000 + 1):
    for mon in xrange(1, 12 + 1):
        if isSunday(1, mon, yr):
            sunCount = sunCount + 1
print(sunCount)
