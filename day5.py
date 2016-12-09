from util import maybe_download
from hashlib import md5

def part1():
    with maybe_download(5) as file:
        s = file.readline().strip()
        i = 0
        password = ''
        while len(password)< 8:
            hash = str(md5((s + str(i)).encode('utf-8')).hexdigest())
            if hash.startswith('00000'):
                password += hash[5]
            i += 1
        print('part1', password)


part1()