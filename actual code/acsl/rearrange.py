def rearrangeString(s, n):
    strings = []
    strings2 = []
    re = ''

    add = False
    if s[-1] != s[-2]:
        add = True

    while len(s) > 1:
        stri = f'{s[0]}'
        while s[0] == s[1]:
            if len(s) == 2:
                stri += s[0]
                break
            stri += s[0]
            s = s[1 : ]
        strings.append(stri)
        s = s[1:]

    if add:
        strings.append(s)

    lengthstring = []
    for i in range(len(strings)):
        lengthstring.append(len(strings[i]))

    value = max(lengthstring)

    while value != 0:
        l = []
        for i in range(0, len(strings)):
            if len(strings[i]) == value:
                l.append(strings[i])
        l.sort()
        for i in range(len(l)):
            re += l[i]
        value -= 1
    
    add2 = False
    if re[-1] != re[-2]:
        add2 = True
    while len(re) > 1:
        stri = f'{re[0]}'
        while re[0] == re[1]:
            if len(re) == 2:
                stri += re[0]
                break
            stri += re[0]
            re = re[1 : ]
        strings2.append(stri)
        re = re[1:]

    if add2:
        strings2.append(re)
    

    for i in range(len(strings2)):
        if len(strings2[i]) > n:
            strings2[i] = strings2[i][0] * n
    
    return ''.join(strings2)

print(rearrangeString('MHHHHJLDDHHDDD', 3))
        