def cows(a, b, c):
    l = [a, b, c]
    l.sort()
    c1 = 0
    c2 = 0

    # shortesttmoves
    if l[2] - l[1] > l[1] - l[0]:
        c1 += l[2] - l[1] - 1
      
    elif l[2] - l[1] < l[1] - l[0]:
        c1 += l[1] - l[0] - 1

    else:
        c1 += l[2] - l[1] - 1
    
    #longest moves

    return c1
print(cows(5, 7, 9))