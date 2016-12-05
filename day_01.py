from util import maybe_download

dirs = 'NESWN'


def next_pos(x, y, dir, op):
    if op[0] == 'R':
        dir = dirs[dirs.index(dir) + 1]
    else:
        dir = dirs[dirs.rindex(dir) - 1]

    n = int(op[1:])

    if dir == 'N':
        y -= n
    elif dir == 'E':
        x += n
    elif dir == 'S':
        y += n
    else:
        x -= n
    return (x, y, dir)


def part1():
    x = 0
    y = 0
    dir = 'N'
    with maybe_download(1) as file:
        data = [s.strip() for s in file.read().split(',')]
        for op in data:
            x, y, dir = next_pos(x, y, dir, op)
        dist = abs(x) + abs(y)
        print('part1:', dist)


part1()

