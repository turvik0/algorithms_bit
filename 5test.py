import numpy as np
from scipy.linalg import circulant

def hadamard_matrix_construction(n):
    assert n % 4 == 0

    sqr_coefs = quadratic_character(n - 1)
 
    res = np.zeros((n, n), dtype=int)
    res[1:, 1:] = circulant(sqr_coefs)
    res[1:, 0] = -1
    res[0, 1:] = 1
    res = res + np.eye(n, dtype=int)

    assert np.all((res == 1) | (res == -1)), f'Matrix is not a Hadamard matrix: {res}'
    return res

def quadratic_character(p):
    sqr = np.arange(p, dtype=int) ** 2 % p
    result = -np.ones(p, dtype=int)
    result[sqr] = 1
    result[0] = 0
    return result

def generate_codes(n):
    codes = hadamard_matrix_construction(n).clip(min=0)
    codes = np.concatenate([
        codes,
        1 - codes,
    ])
    return codes


def print_matrix(a):
    print('\n'.join(''.join(map(str, row)) for row in a))


if __name__ == "__main__":
    n = int(input().strip())
    print_matrix(generate_codes(n))
