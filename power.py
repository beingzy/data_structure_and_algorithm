""" implementation of power function

    Author: Yi Zhang <beingzy@gmail.com>
    Date: 2016/07/15
"""

def power(x, a):
    if a == 0:
        return 1
    elif a < 0:
        return power(1/x, -a)
    elif a > 0:
        return x * power(x, a-1) 