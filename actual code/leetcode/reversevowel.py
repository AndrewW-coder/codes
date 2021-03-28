def reverseVowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    string = []
    l = []
    
    for i in range(len(s)):
        string.append(s[i])
        if s[i] in vowels:
            l.append(s[i])
        
    l.reverse()

    for i in range(len(string)):
        if string[i] in vowels:
            string[i] = l[0]
            l = l[1:]
            
    return ''.join(string)

print(reverseVowels('Aa'))