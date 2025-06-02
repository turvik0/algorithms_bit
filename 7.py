import numpy as np
from scipy.linalg import eigh
def cutspars(endall):
    n = np.max(endall) + 1
    ojctive = np.zeros((n, n), dtype=int)
    ojctive[endall[:, 0], endall[:, 1]] = 1
    ojctive[endall[:, 1], endall[:, 0]] = 1
    setlapp = -ojctive.copy()
    setlapp[range(n), range(n)] = -setlapp.sum(1)
    eigs, v = eigh(setlapp, eigvals_only=False)
    truelist = np.argsort(v[:, 1])
    iflists = [conductt(truelist[:i], truelist[i:], ojctive) for i in range(1, n)]
    _, changeless,changeall = min(iflists, key=lambda t: (t[0], len(t[1]), min(t[1])))
    return changeless,changeall
def conductt(vtes1, vtes2, ojctive):
    assert set(vtes1.tolist() + vtes2.tolist()) == set(list(range(len(ojctive))))
    assert len(vtes1) + len(vtes2) == len(ojctive)
    if len(vtes1) > len(vtes2) or (len(vtes1) == len(vtes2) and min(vtes1) > min(vtes2)):
        vtes1, vtes2 = vtes2, vtes1
    vol = len(vtes1) * len(vtes2)
    answer = ojctive[vtes1][:, vtes2].sum()
    return answer / vol, vtes1, vtes2
if __name__ == '__main__':
    m = int(input().strip())
    endall = np.array([list(map(int, input().strip().split())) for _ in range(m)])
    changeless,changeall = cutspars(endall)
    print(' '.join(map(str, sorted(changeless))))
