import numpy as np
from scipy.optimize import linprog
from scipy.sparse import dok_matrix
num1 = int(input())
masss = [int(input()) for i in range(num1)]
num2 = int(input())
lines = [tuple(map(int, input().split(" "))) for i in range(num2)]
newdict = dok_matrix((len(lines), num1), dtype=np.float32)
for i, boundss in enumerate(lines):
    newdict[i, boundss[0]] = -1
    newdict[i, boundss[1]] = -1
returnanswr = linprog(
    c=masss,
    A_ub=newdict,
    b_ub=[-1] * len(lines),
    bounds=[(0, 1) for i in range(num1)],
    method="interior-point",
    options={"sparse": True, "tol": 1e-2},
)
print(*[i for i, x in enumerate(returnanswr.x) if x >= 0.5], sep=" ")