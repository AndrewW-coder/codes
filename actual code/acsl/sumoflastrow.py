def sumOfLastRow(s, d, r):
    result = 0
    
    m = int((r - 1) * (r) / 2 - 1) #takes all the rows between the last row and the starting value
    n = int(str(s), 8) #base10 value of the starting value
    d = int(str(d), 8) #base 10 value of difference (delta)

    values = [] #placeholder list for the last row numbers

    for i in range(m + 1, m + r + 1): #takes the last rows numbers
        values.append(n + d * i) #puts them in the list

    values = [oct(i).replace('0o', '') for i in values] #converts them to base 8
    
    for i in range(len(values)):
        sum = 0
        p = int(values[i])
        while p > 0:
            f = p % 10
            p = p // 10
            sum += f #takes the sum of the digits
        result += sum #final result

    return result

#############################################################################################################

def sumOfLastRow(s, d, r):
    sd = 0
    dd = 0
    for y in range(1, len(str(s)) + 1):
        sd += int(str(s)[-y]) * 8(y - 1)
    for x in range(1, len(str(d)) + 1):
        dd += int(str(d)[-x]) * 8(x - 1)
    digitsum = 0
    totalsum = 0
    for i in range(1, r + 1):
        totalsum += i
    totalsum -= 1
    biggestn = sd + totalsum * dd
    for i in range(r):
        octbiggestn = oct(biggestn - dd * i)
        for i in range(1, len(octbiggestn) - 1):
            digitsum += int(octbiggestn[-i])
    return digitsum

def sumOfLastRow2(s, d, r):
    result = 0
    
    m = int((r - 1) * (r) / 2 - 1) #takes all the rows between the last row and the starting value
    n = int(str(s), 8) #base10 value of the starting value
    d = int(str(d), 8) #base 10 value of difference (delta)

    for i in range(m + 1, m + r + 1):
        sum = 0 
        p = int(oct(n + d * i).replace('0o', ''))
        while p > 0:
            f = p % 10
            p = p // 10
            sum += f
        result += sum
    return result

print(sumOfLastRow2(2, 3, 5))
        