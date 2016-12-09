from util import maybe_download

def read_line(s):
    lastDash = s.rindex('-')
    checkSumLocation = s.rindex('[')
    name = s[0:lastDash].replace('-', '')
    id = int(s[lastDash + 1:checkSumLocation])
    checksum = s[checkSumLocation + 1:-1]

    return name, id, checksum

def get_checksum(name):
    count = dict()

    for ch in name:
        if ch not in count:
            count[ch] = 1
        else:
            count[ch] = count[ch] + 1
    letters = []
    for ch in count:
        letters.append((99999 - count[ch], ch))

    letters.sort()
    checksum = ''.join([s[1] for s in letters][:5])
    return checksum

def part1():
    total = 0
    with maybe_download(4) as file:
        for s in map(str.rstrip, file):
            name, id, checksum = read_line(s)
            calculated_checksum = get_checksum(name)
            if calculated_checksum == checksum:
                total += id
    print('part1', total)


part1()