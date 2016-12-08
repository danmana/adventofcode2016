from util import maybe_download


def get_code(buttons):
    max_x = len(buttons[0])
    max_y = len(buttons)
    x = None
    y = None

    for yi in range(max_y):
        for xi in range(max_x):
            if buttons[yi][xi] == '5':
                x = xi
                y = yi
                break
        if x is not None:
            break

    code = ''
    with maybe_download(2) as file:
        for s in file:
            for ch in s.strip():
                if ch == 'U' and y - 1 >= 0 and buttons[y - 1][x] != ' ':
                    y -= 1
                elif ch == 'D' and y + 1 < max_y and buttons[y + 1][x] != ' ':
                    y += 1
                elif ch == 'L' and x - 1 >= 0 and buttons[y][x - 1] != ' ':
                    x -= 1
                elif ch == 'R' and x + 1 < max_x and buttons[y][x + 1] != ' ':
                    x += 1
            code += buttons[y][x]
        return code


def part1():
    code = get_code(['123',
                     '456',
                     '789'])
    print('part1:', code)


def part2():
    code = get_code(['  1  ',
                     ' 234 ',
                     '56789',
                     ' ABC ',
                     '  D  '])
    print('part2:', code)


part1()
part2()
