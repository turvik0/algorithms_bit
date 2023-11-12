from typing import List, Union
from random import randint
import sys
def edjeaddd(matt: List[List[int]], v1: int, v2: int, p: int = 9973):
    x = randint(1, p - 1)
    matt[v1][v2] = x

def main():
    _ = int(input())
    vertmaxx = -1
    runegj = []
    for i in sys.stdin:
        if i.strip() == '':
            continue
        v1, v2 = [int(x) for x in i.split()]
        vertmaxx = max(v1, v2, vertmaxx)
        runegj.append((v1, v2))
    numittr = 20
    vertnumbbr = vertmaxx + 1
    for _ in range(numittr):
        matt = [[0] * vertnumbbr for _ in range(vertnumbbr)]
        for v1, v2 in runegj:
            edjeaddd(matt, v1 ,v2)

        evilelemenn = fieldnumrev()
        viewtriangmattto(matt, evilelemenn)
        if not mattsingleh(matt):
            print('yes')
            return
    print('no')

def viewtriangmattto(matt: List[List[int]], evilelemenn: List[int], p: int = 9973):
    matt_size = len(matt)
    for i in range(1, matt_size):
        nmbrcolll = i - 1
        nmbrsaraw = zerorowelm(matt, i - 1, nmbrcolll)
        if nmbrsaraw is None:
            continue
        if nmbrsaraw != i - 1:
            matt[i - 1], matt[nmbrsaraw] = matt[nmbrsaraw], matt[i - 1]

        nmbrsaraw = i - 1
        a = matt[nmbrsaraw][nmbrcolll]
        assert(a > 0 and a < p)
        reverse_a = evilelemenn[a]
        assert(reverse_a > 0 and reverse_a < p)
        for j in range(nmbrsaraw + 1, matt_size):
            b = matt[j][nmbrcolll]
            if b == 0:
                continue
            k = (b * reverse_a) % p
            assert((k * a) % p == b)
            jrownew = []
            for x, y in zip(matt[nmbrsaraw], matt[j]):
                n = (y - k * x) % p
                jrownew.append(n if n >= 0 else p + n)
            matt[j] = jrownew
            assert(matt[j][nmbrcolll] == 0)
    for row in range(matt_size):
        for column in range(matt_size):
            if row > column:
                assert(matt[row][column] == 0)
            else:
                assert(matt[row][column] >= 0)

def zerorowelm(matt: List[List[int]], strtindgz: int, nmbrcolll: int):
    for i in range(strtindgz, len(matt)):
        if matt[i][nmbrcolll] != 0:
            return i
    return None

def fieldnumrev(p: int = 9973):
    nurevsugoi = [-1] * p
    nurevsugoi[1] = 1
    for i in range(2, p):
        nurevsugoi[i] = p - ((p // i) * nurevsugoi[p % i]) % p
        assert((nurevsugoi[i] * i) % p == 1)
    return nurevsugoi

def mattsingleh(matt: List[List[int]]):
    for i in range(len(matt)):
        if matt[i][i] == 0:
            return True
    return False
if __name__ == "__main__":
    main()