from collections import deque


def best_list_pureness(*args):
    resultFormat = 'Best pureness {0} after {1} rotations'

    BestPureness = 0
    BestPurenessRotation = 0
    k = args[1]

    givenList = deque()
    givenList = args[0]

    counter = 0
    for i in range(k+1):

        totalSum = calculateSum(givenList)
        if totalSum > BestPureness:
            BestPureness = totalSum
            BestPurenessRotation = counter
        a = givenList.pop()
        givenList.reverse()
        givenList.append(a)
        givenList.reverse()
        counter += 1

    return resultFormat.format(BestPureness, BestPurenessRotation)


def calculateSum(numbers):
    total = 0
    for number in numbers:
        total += number * numbers.index(number)

    return total