from util import maybe_download


def get_counts(s):
    count = dict()
    for ch in s:
        if ch in count:
            count[ch] += 1
        else:
            count[ch] = 1
    count = [(ch, count[ch]) for ch in count]
    count.sort(key=lambda x: x[1], reverse=True)
    return count

def get_all_counts(file):
    counts = None
    for s in file:
        s = s.strip()
        if counts is None:
            counts = []
            for i in range(len(s)):
                counts.append(dict())
        for i, ch in enumerate(s):
            c = counts[i]
            if ch in c:
                c[ch] += 1
            else:
                c[ch] = 1
    counts = [[(ch, c[ch]) for ch in c] for c in counts]
    for c in counts:
        c.sort(key=lambda x: x[1], reverse=True)
    return counts


def part1():
    with maybe_download(6) as file:
        counts = get_all_counts(file)
        letters = ''.join([c[0][0] for c in counts])
        print('part1', letters)

def part2():
    with maybe_download(6) as file:
        counts = get_all_counts(file)
        letters = ''.join([c[-1][0] for c in counts])
        print('part2', letters)


part1()
part2()
