from collections import deque


def Problem1():
    result = ''
    FirstLine = input()
    SecondLine = input()

    Males = deque()
    Males = FirstLine.split(' ')
    Females = deque()
    Females = SecondLine.split(' ')
    MatchesCount = 0

    while Males and Females:
        FirstFemale = int(Females.pop(0))  # gives first
        LastMale = int(Males.pop())  # gives last

        if LastMale == FirstFemale:
            MatchesCount += 1
            continue

        if LastMale <= 0:
            Females.reverse()
            Females.append(str(FirstFemale))
            Females.reverse()
            continue

        if FirstFemale <= 0:
            Males.append(str(LastMale))
            continue

        if LastMale % 25 == 0:
            Females.reverse()
            Females.append(str(FirstFemale))
            Females.reverse()
            if Males:
                Males.pop()
            continue
        elif FirstFemale % 25 == 0:
            Males.append(str(LastMale))
            if Females:
                Females.pop(0)
            continue

        LastMale -= 2
        Males.append(str(LastMale))

    Males.reverse()
    result += "Matches: {0}\n".format(MatchesCount)
    if Males:
        Males = [int(i) for i in Males]
        result += "Males left: {0}\n".format(str(Males).strip('[]'))
    else:
        result += "Males left: none\n"

    if Females:
        Females = [int(i) for i in Females]
        result += "Females left: {0}\n".format(str(Females).strip('[]'))
    else:
        result += "Females left: none\n"

    print(result)


if __name__ == '__main__':
    Problem1()
