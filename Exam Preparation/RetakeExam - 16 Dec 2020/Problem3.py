def sets(last):
    line = [1, 1]
    inserter = 1

    for i in range(len(last) - 1):
        res = int(last[i]) + int(last[i + 1])
        line.insert(inserter, res)
        inserter += 1

    return line


def get_magic_triangle(*args):
    result = [[1], [1, 1]]

    number = int(args[0])

    for x in range(2, number):
        last = result[-1]
        result.append(sets(last))

    return result


get_magic_triangle(5)
