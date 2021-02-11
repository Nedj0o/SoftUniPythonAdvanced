from collections import deque


def Scheduling():
    Jobs = input()
    IndexofJobToBeDone = int(input())

    JobsList = []
    JobsList = Jobs.split(', ')

    JobsList = [int(i) for i in JobsList]

    Cycles = 0
    Work = True
    var = JobsList[IndexofJobToBeDone]

    while Work:

        a = min(JobsList)

        if a == var:

            Cycles += int(a)
            JobsList.remove(a)
            if a not in JobsList:
                Work = False

        else:
            Cycles += int(a)
            JobsList.remove(a)

    print(Cycles)


if __name__ == '__main__':
    Scheduling()
