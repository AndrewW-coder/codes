def walk(s):
    matrix = []
    s = s.replace(',', ' ')
    s = s.split()
    
    for i in range(8):
        num = str(bin(int(s[i], 16))[2:]) 
        l = []
        for j in range(8 - len(num)):
            l.append(0)
        for j in range(len(num)):
            l.append(int(num[j]))
        matrix.append(l)

    coords = []

    moves = input('Insert moves here: ')
    moves = moves.replace(',', ' ')
    moves = moves.split()

    r = int(moves[0]) 
    c = int(moves[1])

    point = [r, c] 
    

    direction = moves[2]

    firsttime = {
        'L' : 'B',
        'B' : 'R',
        'R' : 'A',
        'A' : 'L'
    }

    secondtime = {
        'L' : 'R',
        'R' : 'L',
        'A' : 'B',
        'B' : 'A'
    }

    thirdtime = {
        'L' : 'A',
        'B' : 'L',
        'R' : 'B',
        'A' : 'R'
    }

    for i in range(int(moves[3])):
        if r > 8:
            r = r % 8
        elif r < 0:
            r = (8 - r) % 8

        if c > 8:
            c = c % 8
        elif c < 0:
            c = (8 - c) % 8

        if matrix[r - 1][c - 1] == 1:
            
            if coords.count(point)/4 % 1 == 0.5:
                direction = thirdtime[direction]

            elif coords.count(point)/4 % 1 == 0.75:
                direction = secondtime[direction]

            elif coords.count(point)/4 % 1 == 0:
                direction = firsttime[direction]


        if direction == 'L':
                c += 1

        elif direction == 'R':
            c -= 1

        elif direction == 'A':
            r -= 1

        elif direction == 'B':
            r += 1

        coords.append(point)
        point = [r, c]


    

    return point
        

    

print(walk('C, C7, 85, D6, 46, D7, E6, 87'))