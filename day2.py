from util import maybe_download

buttons = ['123',
           '456',
           '789']

def part1():
    x = 1
    y = 1
    code = ''
    with maybe_download(2) as file:
        for s in file:
            for ch in s.strip():
                if ch == 'U':
                    y = max(0, y - 1)
                elif ch == 'D':
                    y = min(2, y + 1)
                elif ch == 'L':
                    x = max(0, x - 1)
                elif ch == 'R':
                    x = min(2, x + 1)
            code += buttons[y][x]
        print('part1:', code)


part1()
