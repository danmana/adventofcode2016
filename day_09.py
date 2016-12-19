from util import maybe_download
import re


def decompress_size(s: str, recursive: bool = False):
    text_size = 0
    op_regex = re.compile(r'\((\d+)x(\d+)\)')

    while len(s) != 0:
        m = op_regex.search(s)
        if m is None:
            break

        text_size += m.start()

        n_ch, n = [int(x) for x in m.groups()]

        start_ch = m.end()
        end_ch = start_ch + n_ch

        if recursive:
            chars = s[start_ch: end_ch]
            text_size += decompress_size(chars, recursive) * n
        else:
            text_size += n_ch * n

        s = s[end_ch:]

    text_size += len(s)

    return text_size


def part1():
    with maybe_download(9) as file:
        for s in file:
            s = s.strip()
            print('part1:', decompress_size(s))

def part2():
    with maybe_download(9) as file:
        for s in file:
            s = s.strip()
            print('part2:', decompress_size(s, True))

part1()
part2()
