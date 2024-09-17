import cmath
import math


def my_pi(target_error):
    """
    Implementation of Gauss–Legendre algorithm to approximate PI from https://en.wikipedia.org/wiki/Gauss%E2%80%93Legendre_algorithm

    :param target_error: Desired error for PI estimation
    :return: Approximation of PI to specified error bound
    """
    aN = 1
    bN = 1 / cmath.sqrt(2)
    tN = 1 / 4
    pN = 1
    a1 = 0

    for i in range(1, 10):
        a1 = aN
        aN = (aN + bN) / 2
        bN = (cmath.sqrt(a1 * bN))
        tN = tN - (pN * ((aN - a1) ** 2))
        pN = 2 * pN

    # change this so an actual value is returned
    pi_estimate = ((aN + bN) ** 2) / (4 * tN)
    return pi_estimate



desired_error = 1E-10

approximation = my_pi(desired_error)

print("Solution returned PI=", approximation)

error = abs(math.pi - approximation)

if error < abs(desired_error):
    print("Solution is acceptable")
else:
    print("Solution is not acceptable")
