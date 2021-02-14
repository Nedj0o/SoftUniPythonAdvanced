import math

def FindPlayer(matrix, size, search):
    for row in range(size):
        for col in range(size):
            if matrix[row][col] == search:
                return row, col


def NewPosition(command, curr_pos):
    new_row, new_col = curr_pos[0], curr_pos[1]
    if command == "up":
        new_row -= 1
    elif command == "down":
        new_row += 1
    elif command == "right":
        new_col += 1
    elif command == "left":
        new_col -= 1
    return new_row, new_col


def isInside(row, col, size):
    return 0 <= row < size and 0 <= col < size


def Second():



    SIZE = int(input())
    Board = []
    for i in range(SIZE):
        line = input()
        Board.append(line.split(' '))
    PlayerPos = FindPlayer(Board, SIZE, "P")
    Coins = 0
    result = ''
    YourPath = []


    while Coins < 100:
        command = input()
        if(command == 'right' or command =='left' or command =='up' or command=='down'):
            new_row, new_col = NewPosition(command, PlayerPos)
        else:
            continue

        if not isInside(new_row, new_col, SIZE) or Board[new_row][new_col] == 'X':
            if Coins > 0:
                Coins = math.floor(Coins * 0.5)
            break
        elif Board[new_row][new_col].isnumeric():
            if int(Board[new_row][new_col]) > 0:
                Coins += int(Board[new_row][new_col])
            a = [new_row, new_col]
            YourPath.append(a)

        Board[new_row][new_col] = "P"
        Board[PlayerPos[0]][PlayerPos[1]] = "0"
        PlayerPos = FindPlayer(Board, SIZE, "P")
        if Coins>=100:
            break


    Coins=round(Coins)
    if Coins >= 100:
        result += "You won! You've collected {0} coins.\n".format(Coins)
    else:
        result += "Game over! You've collected {0} coins.\n".format(Coins)

    result += "Your path:\n"

    if YourPath:
        for i in YourPath:
            result += str(i) + '\n'


    print(result)


if __name__ == '__main__':
    Second()
