""" convert numeric number to string in a sepified base 

    Author: Yi Zhang <beingzy@gmail.com>
    Date: 2016/07/15
"""


def numToStr(x, base):
    if x < base:
        return str(x)
    else:
        return numToStr(x // base, base) + str(x % base)