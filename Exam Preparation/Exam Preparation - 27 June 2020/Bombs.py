from collections import deque


def Bombs():
    FirstLine = input()
    SecondLine = input()

    BombEffects = deque()
    BombEffects = FirstLine.split(', ')
    BombCasings = deque()
    BombCasings = SecondLine.split(', ')
    DaturaBombsCount = 0
    CherryBombsCount = 0
    SmokeDecoyBombs = 0
    FilledBombPouch = False
    Result = ''

    while BombEffects and BombCasings and FilledBombPouch is False:

        CurrentBombEffect = BombEffects.pop(0)  # gives first
        CurrentBombCasing = BombCasings.pop()  # gives last
        CurrentBomb = int(CurrentBombEffect) + int(CurrentBombCasing)

        if CurrentBomb == 40:
            DaturaBombsCount += 1
        elif CurrentBomb == 120:
            SmokeDecoyBombs += 1
        elif CurrentBomb == 60:
            CherryBombsCount += 1
        else:
            BombEffects.reverse()
            BombEffects.append(CurrentBombEffect)
            BombEffects.reverse()

            res = int(CurrentBombCasing) - 5
            BombCasings.append(str(res))

        if DaturaBombsCount >= 3 and SmokeDecoyBombs >= 3 and CherryBombsCount >= 3:
            FilledBombPouch = True

    if FilledBombPouch:
        Result += 'Bene! You have successfully filled the bomb pouch!\n'
    else:
        Result += "You don't have enough materials to fill the bomb pouch.\n"

    if not BombEffects:
        Result += "Bomb Effects: empty\n"
    else:
        Result += "Bomb Effects: "
        while BombEffects:
            Result += BombEffects.pop(0)
            if not BombEffects:
                Result += '\n'
            else:
                Result += ', '

    if not BombCasings:
        Result += "Bomb Casings: empty\n"
    else:
        Result += "Bomb Casings: "
        while BombCasings:
            Result += BombCasings.pop(0)
            if not BombCasings:
                Result += '\n'
            else:
                Result += ', '

    Result += "Cherry Bombs: {0}\n".format(CherryBombsCount)
    Result += "Datura Bombs: {0}\n".format(DaturaBombsCount)
    Result += "Smoke Decoy Bombs: {0}\n".format(SmokeDecoyBombs)

    print(Result)


if __name__ == '__main__':
    Bombs()
