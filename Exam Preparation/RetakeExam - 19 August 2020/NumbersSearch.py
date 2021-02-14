import collections


def numbers_searching(*args):
    mylist = list(args)
    Missing = 0

    # finds dublicates in list
    Dublicates = [item for item, count in collections.Counter(mylist).items() if count > 1]
    Dublicates.sort()

    listformissing = list(range(min(mylist), max(mylist)))

    for num in listformissing:
        if num not in mylist:
            Missing = num

    result = [Missing, Dublicates]

    return result
