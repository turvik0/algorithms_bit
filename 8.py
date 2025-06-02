import numpy as np
from itertools import chain, combinations
def getmatt(n):
    edpn = baseclsenum(n)
    getlogg = edpn.bit_length()
    result = np.zeros((getlogg, edpn), dtype=int)
    result[0, :] = 1
    arrsub = np.concatenate([
        np.zeros(edpn >> 1, dtype=int),
        np.ones(edpn >> 1, dtype=int),])
    for i in range(1, getlogg):
        result[i, :] = arrsub.reshape(-1, 1 << (i - 1)).T.reshape(-1)
    return result[:, :n]
def bitwise_xor(listnumm):
    return listnumm.sum(0) % 2
def getbstasign(n, numclaus):
    assert 1 == np.min(np.abs(numclaus))
    assert n == np.max(np.abs(numclaus))
    settmat = getmatt(n)
    bestmaxpossibl = np.zeros(n, dtype=int)
    bestall = clauscorr(bestmaxpossibl, numclaus)
    for i in setpoww(range(len(settmat))):
        if len(i) == 0:
            continue
        nowmaxpossbl = bitwise_xor(settmat[list(i)])
        bestnow = clauscorr(nowmaxpossbl, numclaus)
        if bestnow > bestall:
            bestmaxpossibl = nowmaxpossbl
            bestall = bestnow
    return bestall, bestmaxpossibl
def clauscorr(maxpossibl, numclaus):
    numval = np.take(maxpossibl, np.abs(numclaus) - 1)
    t = np.bitwise_xor(numval, numclaus < 0).any(1).sum()
    return t
def setpoww(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
def baseclsenum(n):
    answer = 1 << (n.bit_length() - 1)
    return answer if answer == n else answer << 1
if __name__ == '__main__':
    n, m = map(int, input().strip().split())
    numclaus = np.array([list(map(int, input().strip().split())) for _ in range(m)])
    _ , maxpossibl = getbstasign(n, numclaus)
    print(''.join(map(str, maxpossibl)))
