from util import maybe_download
import re

def has_abba(s):
    return re.search(r'(.)(?!\1)(.)\2\1', s)

def is_tls(s):
    inner = re.findall('\[(.+?)\]', s)
    outer = re.split('\[.+?\]', s)
    for s in inner:
        if has_abba(s):
            return False
    for s in outer:
        if has_abba(s):
            return True
    return False


def part1():
    with maybe_download(7) as file:
        count = 0
        for s in file:
            s = s.strip()
            if is_tls(s):
                count += 1
        print('part1', count)

part1()