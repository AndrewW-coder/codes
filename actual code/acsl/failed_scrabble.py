def scrabble(word, n, dir):
    word = word.replace(',', ' ')
    word = word.split()
    
    let_val = {
        'A' : 1,
        'E' : 1,
        'D' : 2,
        'R' : 2,
        'B' : 3,
        'M' : 3,
        'V' : 4,
        'Y' : 4,
        'J' : 8,
        'X' : 8
    }

    tiles = []

    if dir == 'H' or dir == 'h':
        for i in range(4):
            tiles.append(n)
            n += 1
    else:
        for i in range(4):
            tiles.append(n)
            n += 10

    dou = 0
    tri = 0
    total = 0

    for i in range(4):
        value = let_val[word[i]]
        if tiles[i] % 6 == 3:
            total += value * 2
        elif tiles[i] % 5 == 0:
            total += value * 3
        elif tiles[i] % 7 == 0:
            dou += 1
        elif tiles[i] % 8 == 0:
            tri += 1
        else:
            total += value

    if dou != 0:
        total *= 2
    if tri != 0 and dou == 0:
        total *= 3

    return total
#print(scrabble('J, A, V, A', 12, 'H'))


#######################################

def digit(num, l):
    total = 0
    word = str(num)
    for i in range(len(word) - l + 1):
        total += int(word[i : i + l])
    return total
    
def digit2(num, n):
    total = 0
    for i in range(len(str(num)) - n + 1):
        total += int(str(num)[i : i + n])
    return total



########################################################


def strfind(str1, str2):
    result = ''
    for i in range(len(str1)):
        if str1[i] in str2:
            result = result + str1[i]
            for j in range(len(str2)):
                if str2[j] == str1[i]:
                    str2 = str2[j:]
    return result

print(strfind('happy', 'shipshape'))