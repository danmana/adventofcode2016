from util import maybe_download
from typing import List
from collections import deque
import re

Display = List[List[int]]


def draw_rect(display: Display, a: int, b: int):
    for y in range(b):
        for x in range(a):
            display[y][x] = 1


def rotate_row(display: Display, a: int, b: int):
    row = deque(display[a])
    row.rotate(b)
    display[a] = list(row)


def rotate_col(display: Display, a: int, b: int):
    col = deque([display[i][a] for i in range(6)])
    col.rotate(b)
    for i in range(6):
        display[i][a] = col[i]


def apply_op(display: Display, s: str):
    if s.startswith('rect'):
        a, b = [int(x) for x in re.match(r'rect (\d+)x(\d+)', s).groups()]
        draw_rect(display, a, b)
    elif s.startswith('rotate column'):
        a, b = [int(x) for x in re.match(r'rotate column x=(\d+) by (\d+)', s).groups()]
        rotate_col(display, a, b)
    elif s.startswith('rotate row'):
        a, b = [int(x) for x in re.match(r'rotate row y=(\d+) by (\d+)', s).groups()]
        rotate_row(display, a, b)


def part1():
    display = [[0 for x in range(50)] for y in range(6)]
    with maybe_download(8) as file:
        for s in file:
            s = s.strip()
            apply_op(display, s)

    on = sum([sum(row) for row in display])
    print('part1', on)


part1()
