"""TestTheComb"""

from math import comb


def wrapper(arg1, arg2):
    if not(isinstance(arg1, int) and isinstance(arg2, int)):
        msg = "must be int, given " + str(type(arg1))
        raise TypeError(msg)
    return comb(int(arg1), int(arg2))


assert(wrapper(10, 5)) == 252
