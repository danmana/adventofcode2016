from util import maybe_download
from hashlib import md5


def next_hash(s, i):
    while True:
        hash = str(md5((s + str(i)).encode('utf-8')).hexdigest())
        i += 1
        if hash.startswith('00000'):
            return (hash, i)


def part1():
    with maybe_download(5) as file:
        s = file.readline().strip()
        i = 0
        password = ''
        while len(password) < 8:
            hash, i = next_hash(s, i)
            password += hash[5]
            print('partial pass', password)
        print('part1', password)


def part2():
    with maybe_download(5) as file:
        s = file.readline().strip()
        i = 0
        password = [' ' for i in range(8)]
        found = 0
        while found < 8:
            hash, i = next_hash(s, i)
            pos = hash[5]
            if pos.isdigit():
                pos = int(pos)
                if pos < 8 and password[pos] == ' ':
                    password[pos] = hash[6]
                    found += 1
                    print('partial pass', ''.join(password))
        print('part2', ''.join(password))


part1()
part2()
