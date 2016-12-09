from util import maybe_download

def is_triangle(a,b,c):
    if a + b <= c:
        return False
    if a + c <= b:
        return False
    if b + c <= a:
        return False
    return True

def part1():
    triangles = 0
    with maybe_download(3) as file:
        for s in file.readlines():
            a,b,c = [int(x) for x in s.split()]
            if is_triangle(a,b,c):
                triangles += 1
        print('part1:', triangles)


part1()