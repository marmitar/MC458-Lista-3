import numpy as np


def base(X, Y):
    _, m1, m2, _ = sorted([X[0], X[1], Y[0], Y[1]])
    return m1, m2

def medianando(X, Y):
    n = len(X)
    if n != len(Y):
        raise ValueError(len(X), len(Y), X, Y)
    elif n == 0:
        return None
    elif n == 1:
        xy = X[0], Y[0]
        return min(xy), max(xy)
    elif n == 2:
        return base(X, Y)

    mx = (n - 1) // 2
    my = n - 1 - mx
    if X[mx] < Y[my]:
        return medianando(X[mx:], Y[:my+1])
    else:
        return medianando(X[:mx+1], Y[my:])

def mediana(X, Y):
    n = len(X)
    if n != len(Y):
        raise ValueError(len(X), len(Y), X, Y)
    elif n == 0:
        raise IndexError('empty')
    elif n == 1:
        return X[0]
    elif n == 2:
        return max(X[0], Y[0])

    mx = (n - 1) // 2
    my = n - 1 - mx
    if X[mx] < Y[my]:
        return mediana(X[mx:], Y[:my+1])
    else:
        return mediana(X[:mx+1], Y[my:])


def gen(n, max=1_000_000):
    v = np.random.randint(max, size=n)
    v.sort()
    return v


def npfind(arr, val1, val2):
    idx = np.argwhere((arr == val1) | (arr == val2))
    if len(idx) == 0:
        return None
    else:
        return int(idx[0])

def npmed(X, Y):
    full = np.concatenate((X, Y))
    full.sort()
    if len(full) == 0:
        return None
    idx = len(full) // 2
    med1, med2 = full[idx-1:idx+1]

    # xi = npfind(X, med1, med2)
    # yi = npfind(Y, med1, med2)
    return med1, med2 #, xi, yi


x, y = gen(100), gen(100)

def regen(n = 100):
    global x, y
    x, y = gen(n), gen(n)


def load(num):
    x = np.load(f'tmp/{num:05d}x.npy')
    y = np.load(f'tmp/{num:05d}y.npy')
    return x, y

def test():
    import os, warnings

    for i in range(1, 10_000):
        max = np.random.randint(10 * i) + 1
        p = np.random.random()
        x, y = gen(i, max), gen(i, max) + int(p * max)

        ans, res = npmed(x, y), mediana(x, y)
        if res not in ans:
            try:
                os.mkdir('tmp')
            except FileExistsError:
                pass

            np.save(f'tmp/{i:05d}x.npy', x)
            np.save(f'tmp/{i:05d}y.npy', y)
            # warnings.warn(f'{i}, {max}, {p}, {ans}, {res}')
            raise ValueError(f'{i}, {max}, {p}, {ans}, {res}')

if __name__ == "__main__":
    test()
