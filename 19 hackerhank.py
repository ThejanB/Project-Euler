# Find Number of Sundays that fell on the first of the month between two dates


def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def zeller_weekday(year, month, day):
    if month < 3:
        month += 12
        year -= 1
    K = year % 100
    J = year // 100
    return (day + (13 * (month + 1)) // 5 + K + (K // 4) + (J // 4) - 2 * J) % 7

def count_sundays(start, end):
    no_of_sundays = 0
    for year in range(start[0], end[0] + 1):
        for month in range(1, 13):
            # Ensure the month is within the valid range
            if (year > start[0] or (year == start[0] and month > start[1])) and \
               (year < end[0] or (year == end[0] and month < end[1])):
                if zeller_weekday(year, month, 1) == 1:  # Sunday (1 in Zeller's Congruence)
                    no_of_sundays += 1
            # Special case: first month is included only if start day is 1
            if year == start[0] and month == start[1] and start[2] == 1:
                if zeller_weekday(year, month, 1) == 1:
                    no_of_sundays += 1
            # Special case: last month is included only if it contains the first day
            if year == end[0] and month == end[1] and end[2] >= 1:
                if zeller_weekday(year, month, 1) == 1:
                    no_of_sundays += 1
    return no_of_sundays
    


date1 = list(map(int, input().split()))
date2 = list(map(int, input().split()))

print(count_sundays(date1, date2))
