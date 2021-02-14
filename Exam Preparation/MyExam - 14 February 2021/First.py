from collections import deque


def First():
    FirstLine = input()
    SecondLine = input()

    Fireworks = deque()
    Fireworks = FirstLine.split(', ')
    ExplosivePower = deque()
    ExplosivePower = SecondLine.split(', ')
    isMariaHappy = False
    result = ''
    PalmFireworks = 0
    WillowFireworks = 0
    CrossetteFireworks = 0

    while ExplosivePower and Fireworks:
        currentFirework = int(Fireworks.pop(0))  # gives first
        currentExplosivePower = int(ExplosivePower.pop())  # gives last

        if currentFirework <= 0:
            ExplosivePower.append(str(currentExplosivePower))
            continue

        if currentExplosivePower <= 0:
            Fireworks.reverse()
            Fireworks.append(str(currentFirework))
            Fireworks.reverse()
            continue

        mix = currentFirework + currentExplosivePower
        if mix % 3 == 0 and mix % 5 != 0:
            PalmFireworks += 1
        elif mix % 5 == 0 and mix % 3 != 0:
            WillowFireworks += 1
        elif mix % 3 == 0 and mix % 5 == 0:
            CrossetteFireworks += 1
        else:
            currentFirework -= 1
            if currentFirework > 0:
                Fireworks.append(str(currentFirework))

            ExplosivePower.append(str(currentExplosivePower))
            continue

        if PalmFireworks >= 3 and WillowFireworks >= 3 and CrossetteFireworks >= 3:
            isMariaHappy = True
            break


    if isMariaHappy:
        result += 'Congrats! You made the perfect firework show!\n'
    else:
        result += 'Sorry. You can’t make the perfect firework show.\n'

    if Fireworks:
        result += 'Fireworks Effects left: '
        Fireworks.reverse()
        while Fireworks:
            result += Fireworks.pop(0)
            if not Fireworks:
                result += '\n'
            else:
                result += ', '

    if ExplosivePower:
        result += 'Explosive Power left: '
        while ExplosivePower:
            result += ExplosivePower.pop(0)
            if not ExplosivePower:
                result += '\n'
            else:
                result += ', '

    result += "Palm Fireworks: {0}\n".format(PalmFireworks)
    result += "Willow Fireworks: {0}\n".format(WillowFireworks)
    result += "Crossette Fireworks: {0}\n".format(CrossetteFireworks)

    print(result)


if __name__ == '__main__':
    First()
