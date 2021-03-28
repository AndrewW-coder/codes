import copy


board = [[str(a + 1) for a in range(b * 3, b * 3 + 3)] for b in range(3)]


def drawBoard(board):
    string = ""
    for i in range(len(board)):
        for j in range(len(board[0])):
            if j < len(board[0]) - 1:
                string += board[i][j] + " | "
            else:
                string += board[i][j]
        if i < len(board) - 1:
            string += "\n" + "-" * ((len(board[0]) * 4) - 3) + "\n"
    return string

def gameOver(board):
    #check diagonals
    if all(board[i][i] == board[0][0] for i in range(3)):
        return board[0][0]
    if all(board[j][2 - j] == board[0][-1] for j in range(3)):
        return board[0][-1]

    #check horizontals
    for k in range(3):
        if all(l == board[k][0] for l in board[k]):
            return board[k][0]

    #check verticals
    for m in range(3):
        if all(n == board[0][m] for n in board[m]):
            return board[0][m]

    #check for empty squares
    empty = False
    for row in board:
        for square in row:
            if square != "O" and square != "X":
                empty = True

    #check for tie
    if not empty:
        return "T"

    return None
    


def findScore(board, turn):
    winner = gameOver(board)
    if winner:
        if winner == "O":
            return 1
        elif winner == "X":
            return -1
        else:
            return 0

    if turn == "O":
        scores = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != "O" and board[i][j] != "X":
                    newBoard = copy.deepcopy(board)
                    newBoard[i][j] = "O"
                    scores.append(findScore(newBoard, "X"))
                    print(turn, i, j, newBoard)
        return max(scores)
    else:
        scores = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != "O" and board[i][j] != "X":
                    newBoard = copy.deepcopy(board)
                    newBoard[i][j] = "X"
                    scores.append(findScore(newBoard, "O"))
                    print(turn, i, j, newBoard)
        return min(scores)

end = False
player = "X"

while not end:
    if player == 'X':
        print(drawBoard(board))
        
        s = " "
        while s == "O" or s == "X" or all(s not in sublist for sublist in board):
            s = input(f"{player}'s turn: ")   
        s = int(s) - 1

        board[s // 3][s - (s // 3 * 3)] = player
    else:
        max_score = -2
        max_x = max_y = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != "O" and board[i][j] != "X":
                    newBoard = copy.deepcopy(board)
                    newBoard[i][j] = "O"
                    score = findScore(board, "X")
                    if score > max_score:
                        max_score = score
                        max_x = i
                        max_y = j
        board[max_x][max_y] = "O"

    if player == "O":
        player = "X"
    else:
        player = "O"



    winner = gameOver(board)
    if winner:
        if winner == "T":
            print(drawBoard(board))
            print("Tie!")
            end = True
        else:
            print(drawBoard(board))
            print(f"{winner} won!")
            end = True
        