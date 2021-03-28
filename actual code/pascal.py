def pascal(r):
    if r == 1:
        return [[1]]
    if r == 2:
        return [[1], [1, 1]]
    re = [[1], [1, 1]]
    counter = 0
    while counter < r - 1:
        line = [1]
        for i in range(len(re[-1]) - 1):
            line.append(re[-1][i] + re[-1][i + 1])
        line.append(1)
        re.append(line)
        counter += 1

    return re

print(pascal(4))