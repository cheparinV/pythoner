import random
import matplotlib.pyplot as plt
import numpy as np
import math


def toBinary(n):
    s = 0
    while n % 2 == 0:
        s += 1
        n = n / 2
    return s, n


def arrayCount(array):
    res = []
    for i in xrange(1000, 10000, 1000):
        j = i - 1000
        count = len([a for a in array if i > a > j])
        res.append(count)
    return res


def MillerRabin(n, c=20):
    res = []
    s, t = toBinary(n - 1)
    for i in xrange(1, c):
        a = random.randint(2, n - 1)
        if n % a == 0:
            return True
        b = pow(a, t, n)
        if b == n - 1 or b == 1:
            res.append(a)
            continue
        for j in xrange(0, s - 1):
            b = pow(b, 2, n)
            if b == n - 1 or b == 1:
                res.append(a)
                break
        if b != n - 1 & b != 1:
            return True
    return res


prime = 10337
array = MillerRabin(prime, int(math.log(prime)))
y = arrayCount(array)
x = xrange(1000, 10000, 1000)
print y
plt.plot(x, y)
plt.show()