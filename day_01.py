from util import maybe_download

dirs = 'NESWN'

def next_dir(dir, op):
    if op[0] == 'R':
        return dirs[dirs.index(dir) + 1]
    else:
        return dirs[dirs.rindex(dir) - 1]

def next_pos(x,y, dir, n):
    if dir == 'N':
        y -= n
    elif dir == 'E':
        x += n
    elif dir == 'S':
        y += n
    else:
        x -= n
    return (x,y)


def fast_forward(x, y, dir, op):
    dir = next_dir(dir, op)

    n = int(op[1:])

    x,y = next_pos(x, y, dir, n)

    return (x, y, dir)


def part1():
    x = 0
    y = 0
    dir = 'N'
    with maybe_download(1) as file:
        data = [s.strip() for s in file.read().split(',')]

        for op in data:
            x, y, dir = fast_forward(x, y, dir, op)

        dist = abs(x) + abs(y)
        print('part1:', dist)


def part2():
    visited = set()
    x = 0
    y = 0
    dir = 'N'
    visited.add((x,y))
    with maybe_download(1) as file:
        data = [s.strip() for s in file.read().split(',')]

        for op in data:
            dir = next_dir(dir, op)
            n = int(op[1:])
            for i in range(n):
                x,y = next_pos(x,y,dir,1)
                if (x,y) in visited:
                    dist = abs(x) + abs(y)
                    print('part1:', dist)
                    return
                else:
                    visited.add((x,y))

part1()
part2()

