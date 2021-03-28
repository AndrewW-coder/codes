def date(date1, date2):
    days = 0
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    leapmonths = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    date1 = date1.replace('-', ' ')
    date2 = date2.replace('-', ' ')

    date1 = date1.split()
    date2 = date2.split()

    date1 = [int(i) for i in date1]
    date2 = [int(i) for i in date2]

    if date1[0] > date2[0]:
        
        
    if date1[0] < date2[0]:
        
###############################################
    else:
        l = [date1[1], date2[1]]
        
        if date1[0] % 4 == 0:
            for i in range(min(l) - 1, max(l) - 1):
                days += leapmonths[i]
        else:
            for i in range(min(l) - 1, max(l) - 1):
                days += months[i]

        if date1[1] > date2[1]:
            days += date1[2]
            days -= date2[2]
        elif date2[1] > date1[1]:
            days += date2[2]
            days -= date1[2]
        else:
            days += abs(date2[2] - date1[2])



    return days

print(date('2020-11-29', '2020-12-13'))