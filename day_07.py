from util import maybe_download
import re


def has_abba(s):
    return re.search(r'(.)(?!\1)(.)\2\1', s)


def split_ip(s):
    hypernet = re.findall(r'\[(.+?)\]', s)
    supernet = re.split(r'\[.+?\]', s)
    return hypernet, supernet


def is_tls(s):
    hypernet, supernet = split_ip(s)
    for s in hypernet:
        if has_abba(s):
            return False
    for s in supernet:
        if has_abba(s):
            return True
    return False

def get_abas(words):
    abas = []
    for w in words:
        for i in range(len(w)-2):
            if w[i] != w[i+1] and w[i] == w[i+2]:
                abas.append(w[i:i+3])
    return set(abas)

def is_ssl(s):
    hypernet, supernet = split_ip(s)
    abas_h = get_abas(hypernet)
    abas_s = get_abas(supernet)
    for aba in abas_h:
        bab = aba[1] + aba[0] + aba[1]
        if bab in abas_s:
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


def part2():
    with maybe_download(7) as file:
        count = 0
        for s in file:
            s = s.strip()
            if is_ssl(s):
                count += 1
        print('part2', count)


part1()
part2()
