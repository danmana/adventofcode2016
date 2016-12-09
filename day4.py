from util import maybe_download

def read_line(s):
    lastDash = s.rindex('-')
    checkSumLocation = s.rindex('[')
    name = s[0:lastDash].replace('-', ' ')
    id = int(s[lastDash + 1:checkSumLocation])
    checksum = s[checkSumLocation + 1:-1]

    return name, id, checksum

def get_checksum(name):
    count = dict()
    name = name.replace(' ', '')

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

def decrypt(name, id):
    real_name = ''
    ord_a = ord('a')
    ord_z = ord('z')
    max_letters = ord_z - ord_a + 1

    for ch in name:
        if ch != ' ':
            ch = chr(ord_a + (ord(ch)-ord_a + id) % max_letters)
        real_name += ch
    return real_name

def part2():
    with maybe_download(4) as file:
        for s in map(str.rstrip, file):
            name, id, checksum = read_line(s)
            calculated_checksum = get_checksum(name)
            if calculated_checksum == checksum:
                real_name = decrypt(name, id)
                if real_name.find('north') != -1:
                    print(real_name, id)



part1()
part2()