def countLargestGroup(n):
    l = []
    re = []
    for i in range(1, n + 1):
        sum = 0
        while i > 0:
            d = i % 10
            i = i//10
            sum += d
        l.append(sum)
    
    print(l)
   
    for i in range(0, len(l)):
        while len(l) > 0:
            re.append(l.count(l[i]))
            l.remove(l[i])
    print(re)

        
    return re.count(max(re))



    
print(countLargestGroup(1))