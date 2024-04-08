import math
import sympy as sp
from sympy.utilities.lambdify import lambdify
from colors import bcolors


def trapezoidal_rule(f, a, b, n):

    h = (b - a) / n
    T = f(a) + f(b)
    integral = 0.5 * T

    for i in range(1, n):
        x_i = a + i * h
        integral += f(x_i)

    integral *= h

    return integral


def calc_trapez():
    print(bcolors.HEADER, "due to discontinuity of the given function. domain was divided to 2 and integral is approximate by 0.2 ")
    func = lambda x: (2 * x ** 2 + math.cos(2 * math.e ** (-2 * x))) / (2 * x ** 3 + x ** 2 - 6)
    x1, x2 = -0.6, 2.9
    y1 = 1.2933
    y2 = 1.30001
    n1 = 501  # Starting value of n



    result1 = trapezoidal_rule(func, x1, y1, n1)
    result2 = trapezoidal_rule(func, y2, x2, n1)
    integral = result1 + result2


    print(bcolors.OKBLUE,"n=" + str(n1))

    print(bcolors.OKBLUE, "Approximate integral:", integral, bcolors.ENDC)



if __name__ == '__main__':
    calc_trapez()
