from util import maybe_download
import re


def decompress_size(s):
    text_size = 0
    op_regex = re.compile(r'\((\d+)x(\d+)\)')

    while len(s) != 0:
        m = op_regex.search(s)
        if m is None:
            break

        text_size += m.start()

        n_ch, n = [int(x) for x in m.groups()]

        text_size += n_ch * n

        start_ch = m.end()
        end_ch = start_ch + n_ch

        s = s[end_ch:]

    text_size += len(s)

    return text_size


def part1():
    with maybe_download(9) as file:
        for s in file:
            s = s.strip()
            print('part1:', decompress_size(s))


part1()
