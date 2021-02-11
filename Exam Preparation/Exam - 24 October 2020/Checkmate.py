def FindPosition(matrix, size, symbol):
    positions = []
    for row in range(size):
        for col in range(size):
            if matrix[row][col] == symbol:
                positions.append([row, col])
    return positions


def isPositionValid(row, col, size):
    return 0 <= row < size and 0 <= col < size


CHANGES = {
    "up": (-1, 0),
    "down": (1, 0),
    "right": (0, 1),
    "left": (0, -1),
    "up-left": (-1, -1),
    "down-left": (1, -1),
    "up-right": (-1, 1),
    "down-right": (1, 1),
}


def CheckForCheckmate(queen_pos, size, matrix):
    for direction in CHANGES:
        q_row, q_col = queen_pos[0], queen_pos[1]
        change_row, change_col = CHANGES[direction][0], CHANGES[direction][1]
        while isPositionValid(q_row + change_row, q_col + change_col, size):
            q_row += change_row
            q_col += change_col
            if matrix[q_row][q_col] == "Q":
                break
            elif matrix[q_row][q_col] == "K":
                return True
    return False


def CheckMate():
    SIZE = 8
    Board = [input().split() for _ in range(SIZE)]
    KingPosition = FindPosition(Board, SIZE, "K")[0]
    QueenPositions = FindPosition(Board, SIZE, "Q")
    WinnerQueens = []

    for queen in QueenPositions:
        if CheckForCheckmate(queen, SIZE, Board):
            WinnerQueens.append(queen)

    if WinnerQueens:
        [print(queen) for queen in WinnerQueens]
    else:
        print("The king is safe!")


if __name__ == '__main__':
    CheckMate()
