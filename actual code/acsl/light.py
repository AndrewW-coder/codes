def lights_out(n):
    counter = 0
    n = n.split()
    n = [int(i) for i in n]
    

    matrix = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
    ]

    
    for i in range(1, 1 + n[0]):
        for j in range(1, len(str(n[i]))):
            r = int(str(n[i])[0]) - 1
            c = int(str(n[i])[j]) - 1

            matrix[r][c] = 1 - matrix[r][c]

    n = n[n[0] + 1:]

    for i in range(1, 1 + n[0]):
        r = int(str(n[i])[0]) - 1
        c = int(str(n[i])[1]) - 1

        matrix[r][c] = 1 - matrix[r][c]

        if r >= 2 and r <= 5:
            matrix[r + 1][c] = 1 - matrix[r + 1][c]
            matrix[r - 1][c] = 1 - matrix[r - 1][c]
            matrix[r + 2][c] = 1 - matrix[r + 2][c]
            matrix[r - 2][c] = 1 - matrix[r - 2][c]
        else:
            if r == 0:
                matrix[r + 1][c] = 1 - matrix[r + 1][c]
                matrix[r + 2][c] = 1 - matrix[r + 2][c]

            elif r == 1:
                matrix[r + 1][c] = 1 - matrix[r + 1][c]
                matrix[r + 2][c] = 1 - matrix[r + 2][c]
                matrix[r - 1][c] = 1 - matrix[r - 1][c]
               
            elif r == 6:
                matrix[r + 1][c] = 1 - matrix[r + 1][c]
                matrix[r - 1][c] = 1 - matrix[r - 1][c]
                matrix[r - 2][c] = 1 - matrix[r - 2][c]
            
            elif r == 7:
                matrix[r - 1][c] = 1 - matrix[r - 1][c]
                matrix[r - 2][c] = 1 - matrix[r - 2][c]

        if c >= 2 and c <= 5:
            matrix[r][c + 1] = 1 - matrix[r][c + 1]
            matrix[r][c - 1] = 1 - matrix[r][c - 1]
            matrix[r][c + 2] = 1 - matrix[r][c + 2]
            matrix[r][c - 2] = 1 - matrix[r][c - 2]
        else:
            if c == 0:
                matrix[r][c + 1] = 1 - matrix[r][c + 1]
                matrix[r][c + 2] = 1 - matrix[r][c + 2]

            elif c == 1:
                matrix[r][c + 1] = 1 - matrix[r][c + 1]
                matrix[r][c + 2] = 1 - matrix[r][c + 2]
                matrix[r][c - 1] = 1 - matrix[r][c - 1]

            elif c == 6:
                matrix[r][c + 1] = 1 - matrix[r][c + 1]
                matrix[r][c - 1] = 1 - matrix[r][c - 1]
                matrix[r][c - 2] = 1 - matrix[r][c - 2]

            elif c == 7:
                matrix[r][c - 1] = 1 - matrix[r][c - 1]
                matrix[r][c - 2] = 1 - matrix[r][c - 2]

        if r >= 1 and r <= 6 and c >= 1 and c <= 6:
            matrix[r + 1][c + 1] = 1 - matrix[r + 1][c + 1]
            matrix[r - 1][c + 1] = 1 - matrix[r - 1][c + 1]
            matrix[r + 1][c - 1] = 1 - matrix[r + 1][c - 1]
            matrix[r - 1][c - 1] = 1 - matrix[r - 1][c - 1]
        else:
            if r == 0 and c >= 1 and c <= 6:
                matrix[r + 1][c + 1] = 1 - matrix[r + 1][c + 1]
                matrix[r + 1][c - 1] = 1 - matrix[r + 1][c - 1]

            elif c == 0 and r >= 1 and r <= 6:
                matrix[r + 1][c + 1] = 1 - matrix[r + 1][c + 1]
                matrix[r - 1][c + 1] = 1 - matrix[r - 1][c + 1]

            elif r == 7 and c >= 1 and c <= 6:
                matrix[r - 1][c + 1] = 1 - matrix[r - 1][c + 1]
                matrix[r - 1][c - 1] = 1 - matrix[r - 1][c - 1]

            elif c == 7 and r >= 1 and r <= 6:
                matrix[r + 1][c - 1] = 1 - matrix[r + 1][c - 1]
                matrix[r - 1][c - 1] = 1 - matrix[r - 1][c - 1]
            
            elif c == 0 and r == 0:
                matrix[r + 1][c + 1] = 1 - matrix[r + 1][c + 1]

            elif c == 0 and r == 7:
                matrix[r - 1][c + 1] = 1 - matrix[r - 1][c + 1]

            elif c == 7 and r == 0:
                matrix[r + 1][c - 1] = 1 - matrix[r + 1][c - 1]
            
            elif c == 7 and r == 7:
                matrix[r - 1][c - 1] = 1 - matrix[r - 1][c - 1]


    for i in matrix:
        counter += i.count(1)
        
    return counter

# print(lights_out('2 434 523 1 43'))
# print(lights_out('1 58 1 58'))
# print(lights_out('1 58 1 57'))
# print(lights_out('3 32 44 56 2 54 18'))

