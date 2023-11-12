import numpy as np
def ccreatelaww(numlaw):
    basa = genhamm(numlaw)
    hadflip = np.flipud(basa)
    inversesmth = elinvcom(basa)
    hadcombine = np.vstack((inversesmth, hadflip))
    hadmresult(hadcombine)

def hadmresult(hadmattr):
    hadmattr = hadmattr.astype(int)
    for row in hadmattr:
        print(' '.join(map(str, row)))

def genhamm(numlaw):
    patthamm = np.ones((numlaw, numlaw))
    numres = numlaw - 1
    ress = np.full(numres * 2, -1)
    for idx in range(1, (numres // 2) + 1):
        ress[(idx * idx) % numres] = 1
    ress[numres:] = ress[:numres]
    for row in range(1, numlaw):
        for col in range(1, numlaw):
            patthamm[row, col] = ress[col - row + numres]
    return patthamm

def elinvcom(mattr):
    return np.where(mattr % 2 == 0, mattr, 0)
if __name__ == "__main__":
    resultnumlaw = int(input("Enter the numlaw of the Hadamard mattrix: "))
    ccreatelaww(resultnumlaw)