from util import maybe_download


def is_triangle(a, b, c):
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
            a, b, c = [int(x) for x in s.split()]
            if is_triangle(a, b, c):
                triangles += 1
        print('part1:', triangles)


def part2():
    triangles = 0
    s1 = []
    s2 = []
    s3 = []
    with maybe_download(3) as file:
        for s in file.readlines():
            a, b, c = [int(x) for x in s.split()]
            s1.append(a)
            s2.append(b)
            s3.append(c)
        for i in range(0, len(s1), 3):
            a, b, c = s1[i:i + 3]
            if is_triangle(a, b, c):
                triangles += 1
            a, b, c = s2[i:i + 3]
            if is_triangle(a, b, c):
                triangles += 1
            a, b, c = s3[i:i + 3]
            if is_triangle(a, b, c):
                triangles += 1
        print('part2:', triangles)


part1()
part2()
