def wordPattern(pattern, s):
    l1 = s.split()
    l2 = []
    

    for i in range(0, len(pattern)):
        l2.append(pattern[i])

    print(l1)
    print(l2)

    if len(l1) != len(l2):
        return False
    
    for i in range(0, len(pattern)):
        if l1.index(f'{l1[i]}') != l2.index(f'{l2[i]}'):
            return False
    return True

print(wordPattern('aaa', 'aa aa aa aa'))