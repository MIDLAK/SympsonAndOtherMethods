import numpy as np
from math import *
from Interval import Interval

def simpson(func: str, interval: Interval, step: float) -> float:
    s = 0.0
    i = 0 # счётчик
    for x in np.arange(interval.left, interval.right, step):
        if i%2 == 0:
            s = s + 4 * eval(func)
        else:
            s = s + 2 * eval(func)
        i = i + 1

    x = interval.left
    func_left_value = eval(func)
    x = interval.right
    func_right_value = eval(func)

    s = step/3 * (func_left_value + func_right_value + s)
    return s
