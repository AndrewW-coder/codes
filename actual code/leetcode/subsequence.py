def isSubsequence(s, t):
    tlist = []
    for i in range(len(t)):
        if t[i] in s:
            tlist.append(t[i])

    if tlist == []:
        return False


    while len(s) > 0:
        if tlist.count(s[0]) == 0 or len(s) > 0 and len(tlist) == 0:
            return False
        for i in range(0, len(tlist)):
            if tlist[i] == s[0]:
                tlist = tlist[i + 1:]
                s = s[1:]     
                break       
                
    return True

print(isSubsequence('acb', 'ahbgdc'))